"""
DAG for pulling the historical weather data for training the ML model.
"""

from datetime import datetime, timezone
import hashlib
import json
import logging
import os
import time
from typing import cast

from airflow import DAG
from airflow.models.param import ParamsDict, Param
from airflow.providers.standard.operators.python import PythonOperator
import requests

from src.utils.sign_manifest import sign_manifest
from src.utils.verify_manifest import verify_manifest


logger = logging.getLogger(__name__)


def ping_rest_api(
    base_url: str = "https://archive-api.open-meteo.com/v1/archive?latitude=53.5511&longitude=9.9937&start_date=2023-01-01&end_date=2023-01-01&daily=temperature_2m_mean&timezone=UTC",
    timeout: int = 10,
    **context
) -> None:
    """
    Confirms the REST API is reachable.
    Raises RuntimeError on failure.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number - 1,
    }

    logger.info("Starting REST API health check", extra={
        "base_url": base_url,
        "timeout": timeout,
        **log_context,
    })

    try:
        start = time.time()

        response = requests.get(base_url, timeout=timeout)
        response.raise_for_status()

        response_time_ms = (time.time() - start) * 1000

        logger.info("REST API health check successful", extra={
            "http_method": "GET",
            "url": base_url,
            "status_code": response.status_code,
            "response_time_ms": response_time_ms,
            **log_context,
        })
        if response_time_ms > 2000:
            logger.warning("REST API slow response", extra={
                "url": base_url,
                "response_time_ms": response_time_ms,
                "threshold_ms": 2000,
                **log_context,
            })
        safe_headers = {
            k: v for k, v in response.headers.items()
            if k.lower() in ["content-type", "content-length"]
        }
        logger.debug("REST API raw response details", extra={
            "url": base_url,
            "headers": safe_headers,
            "content_length": len(response.content),
            **log_context,
        })

    except requests.exceptions.ConnectionError as exc:
        logger.error("REST API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })
        
        raise RuntimeError(
            f"REST API unreachable - connection failed: {base_url}"
        ) from exc
    
    except requests.exceptions.Timeout as exc:
        logger.error("REST API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })

        raise RuntimeError(
            f"STA API unreachable - timed out after {timeout}s: {base_url}"
        ) from exc
    
    except requests.exceptions.HTTPError as exc:
        logger.error("REST API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })

        raise RuntimeError(
            f"REST API returned unexpected status {exc.response.status_code}: {base_url}"
        ) from exc


def fetch_rest_api_data(
    base_url: str = "https://archive-api.open-meteo.com/v1/archive",
    **context
) -> None:
    """
    Fetches selected data for the requested data range.
    Writes one JSON file and a manifest file for auditability.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number - 1,
    }
    query_params = {
        "latitude": context["params"]["latitude"],
        "longitude": context["params"]["longitude"],
        "start_date": context["params"]["start_date"],
        "end_date": context["params"]["end_date"],
        "daily": context["params"]["daily"],
        "timezone": context["params"]["timezone"],
    }

    logger.info("Starting fetching data", extra={
        **query_params,
        **log_context,
    })

    os.makedirs("data/raw/weather", exist_ok=True)
    run_ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest = {
        # Run identify
        "schema_version": "1.0",
        "run_ts": run_ts,
        **log_context,
        "triggered_by": (
            str(dag_run.triggering_user_name)
            if hasattr(dag_run, "triggering_user_name") else "unknown"
        ),

        # Inputs
        "source_url": base_url,
        "query_params": query_params,

        # Log correlation
        "log_ref": {
            "log_file": "/opt/airflow/logs/dag_runs.jsonl",
            "filter": {
                "run_id": dag_run.run_id,
                "dag_id": dag_run.dag_id,
            }
        },

        # Outputs
        "files": [],
    }

    try:
        response = requests.get(base_url, params=query_params, timeout=30)
        response.raise_for_status()

        filename = f"data/raw/weather/weather_{run_ts}.json"
        payload = json.dumps(
            response.json(),
            ensure_ascii=False,
            indent=2
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(payload)
        
        checksum = hashlib.sha256(payload.encode()).hexdigest()
        manifest["files"].append({
            "filename":         filename,
            "checksum_sha256":  checksum,
        })

        manifest = sign_manifest(manifest)
        if not verify_manifest(manifest, pub_key_path="config/manifest_signing.pub"):
            raise RuntimeError("Manifest signature verification failed")
        
        manifest_path = f"data/raw/weather/manifest_{run_ts}.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        context["ti"].xcom_push(key="manifest", value=manifest)

        logger.info("Fetching data successful", extra={
            "data_file": filename,
            "checksum_sha256": checksum,
            "manifest_path": manifest_path,
            **query_params,
            **log_context,
        })

    except requests.exceptions.RequestException as exc:
        logger.error(f"Fetching data failed: {exc}", extra={
            **query_params,
            **log_context,
        })
        raise


def validate_data_file(**context) -> None:
    """
    Checks that data file contains features.
    Stores name of problematic data file.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number - 1,
    }

    manifest = context["ti"].xcom_pull(
        task_ids="fetch_rest_api_data", key="manifest"
    )

    logger.info("Starting data file validation", extra={
        **log_context,
    })

    file_name = manifest["files"][0]["filename"]
    file_problematic = False
    with open(file_name, "r") as f:
        file_content = json.load(f)
    for daily in context["params"]["daily"]:
        if file_content["daily"].get(daily) is None:
            file_problematic = True
            break
    
    if file_problematic:
        problematic_file = file_name

        with open("data/raw/weather/problematic_files.json", "w") as f:
            f.write(json.dumps(problematic_file))
        
        logger.warning("Problematic file discovered", extra={
            "filename": problematic_file,
            **log_context,
        })


with DAG(
    dag_id="training_weather_data_pull",
    start_date=datetime(2026, 4, 23),
    schedule=None,
    catchup=False,
    params=cast(ParamsDict, {
        "latitude": Param(53.5511, type="number"),
        "longitude": Param(9.9937, type="number"),
        "start_date": Param("2023-01-01", type="string"),
        "end_date": Param("2025-12-31", type="string"),
        "daily": Param([
            "wind_gusts_10m_max",
            "wind_speed_10m_mean",
            "precipitation_sum",
            "sunshine_duration",
            "cloud_cover_mean",
            "temperature_2m_mean",
            "relative_humidity_2m_mean",
        ], type="array", items={"type": "string"}),
        "timezone": Param("Europe/Berlin", type="string")
    })
) as dag:
    
    ping_task = PythonOperator(
        task_id="ping_rest_api",
        python_callable=ping_rest_api
    )

    extract_task = PythonOperator(
        task_id="fetch_rest_api_data",
        python_callable=fetch_rest_api_data
    )

    validate_task = PythonOperator(
        task_id="validate_data_file",
        python_callable=validate_data_file
    )

    ping_task >> extract_task >> validate_task
