"""
DAG for pulling historical bicycle traffic data for training the ML model.
"""

from datetime import datetime, timezone
import hashlib
import json
import logging
import os
import time
from urllib.parse import quote

from airflow import DAG
from airflow.models.param import Param
from airflow.operators.python import PythonOperator
import requests

from src.utils.sign_manifest import sign_manifest
from src.utils.verify_manifest import verify_manifest


logger = logging.getLogger(__name__)


def ping_sta_api(
        base_url: str = "https://iot.hamburg.de/v1.1",
        timeout: int = 10,
        **context
    ) -> None:
    """
    Confirms the STA API is reachable.
    Raises RuntimeError on failure.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number,
    }

    logger.info("Starting STA API health check", extra={
        "base_url": base_url,
        "timeout": timeout,
        **log_context,
    })

    try:
        start = time.time()

        response = requests.get(base_url, timeout=timeout)
        response.raise_for_status()

        response_time_ms = (time.time() - start) * 1000

        logger.info("STA API health check successful", extra={
            "http_method": "GET",
            "url": base_url,
            "status_code": response.status_code,
            "response_time_ms": response_time_ms,
            **log_context,
        })
        if response_time_ms > 2000:
            logger.warning("STA API slow response", extra={
                "url": base_url,
                "response_time_ms": response_time_ms,
                "threshold_ms": 2000,
                **log_context,
            })
        safe_headers = {
            k: v for k, v in response.headers.items()
            if k.lower() in ["content-type", "content-length"]
        }
        logger.debug("STA API raw response details", extra={
            "url": base_url,
            "headers": safe_headers,
            "content_length": len(response.content),
            **log_context,
        })
    
    except requests.exceptions.ConnectionError as exc:
        logger.error("STA API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })
        raise RuntimeError(
            f"STA API unreachable - connection failed: {base_url}"
        ) from exc
    
    except requests.exceptions.Timeout as exc:
        logger.error("STA API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })
        raise RuntimeError(
            f"STA API unreachable - timed out after {timeout}s: {base_url}"
        ) from exc
    
    except requests.exceptions.HTTPError as exc:
        logger.error("STA API health check failed", extra={
            "base_url": base_url,
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            **log_context,
        })
        raise RuntimeError(
            f"STA API returned unexpected status {exc.response.status_code}: {base_url}"
        ) from exc


def paginate(url: str, timeout: int = 30) -> list:
    """
    Follows @iot.nextLink until exhausted.
    Returns all items.
    """

    logger.info("Starting pagination", extra={
        "url": url,
        "timeout": timeout,
    })

    results = []
    next_url = url
    while next_url:
        response = requests.get(next_url, timeout=timeout)
        response.raise_for_status()
        body = response.json()
        results.extend(body.get("value", []))
        next_url = body.get("@iot.nextLink")
    
    logger.info("Pagination completed", extra={
        "total_items": len(results)
    })

    return results


def discover_datastreams(**context) -> list:
    """
    Returns a list of Datastream IDs for the target service and layer.
    Pushes results to XCom for the extract task.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number,
    }

    
    layer_name = context["params"]["layer_name"]
    filter_expr = (
        f"properties/serviceName eq 'HH_STA_HamburgerRadzaehlnetz' "
        f"and properties/layerName eq '{layer_name}'"
    )
    url = (
        f"https://iot.hamburg.de/v1.1/Datastreams"
        f"?$filter={quote(filter_expr)}"
        f"&$select=@iot.id,name"
        f"&$top=1000"
    )

    logger.info("Starting discovery of datastreams", extra={
        "url": url,
        **log_context,
    })

    datastreams = paginate(url)
    
    if not datastreams:
        logger.warning("No Datastreams found", extra={
            "layer_name": layer_name,
            **log_context,
        })

        raise ValueError(f"No Datastreams found for layer: {layer_name}")
    
    ids = [ds["@iot.id"] for ds in datastreams]
    context["ti"].xcom_push(key="datastream_ids", value=ids)

    logger.info("Discovery of datastreams successful", extra={
        "datastream_count": len(ids),
        **log_context,
    })

    return ids


def fetch_sta_api_data(**context) -> None:
    """
    Fetches all observations for each discovered datastream within the
    requested data range.
    Writes one JSON file per datastream and a manifest file for auditability.
    """

    dag_run = context["dag_run"]
    task_instance = context["ti"]
    log_context = {
        "dag_id": dag_run.dag_id,
        "run_id": dag_run.run_id,
        "task_id": task_instance.task_id,
        "retry_attempt": task_instance.try_number,
    }

    start_date = context["params"]["start_date"]
    end_date = context["params"]["end_date"]
    datastream_ids = context["ti"].xcom_pull(
        task_ids="discover_datastreams", key="datastream_ids"
    )

    logger.info("Starting fetching data", extra={
        "data_start_date": start_date,
        "data_end_date": end_date,
        "datastream_ids": datastream_ids,
        **log_context,
    })

    os.makedirs("data/raw/bicycle", exist_ok=True)
    run_ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest = {
        # Run identity
        "schema_version": "1.0",
        "run_ts": run_ts,
        **log_context,
        "triggered_by": (
            str(dag_run.triggering_user_name)
            if hasattr(dag_run, "triggering_user_name") else "unknown"
        ),

        # Inputs
        "inputs": {
            "start_date": start_date,
            "end_date": end_date,
            "layer_name": context["params"]["layer_name"],
            "source_url": "https://iot.hamburg.de/v1.1",
            "datastream_ids": datastream_ids,
        },

        # Log correlation
        "log_ref": {
            "log_file": "opt/airflow/logs/dag_runs.jsonl",
            "filter": {
                "run_id": dag_run.run_id,
                "dag_id": dag_run.dag_id,
            }
        },

        # Outputs
        "files": [],
    }

    for ds_id in datastream_ids:
        filter_expr = (
            f"phenomenonTime ge {start_date}T00:00:00Z "
            f"and phenomenonTime le {end_date}T23:59:59Z"
        )
        url = (
            f"https://iot.hamburg.de/v1.1/Datastreams({ds_id})/Observations"
            f"?$filter={quote(filter_expr)}"
            f"&$orderBy=phenomenonTime asc"
            f"&$top=1000"
        )

        logger.info("Start fetching observations for datastream", extra={
            "datastream_id": ds_id,
            "url": url,
            **log_context,
        })

        observations = paginate(url)

        filename = f"data/raw/bicycle/bicycle_{ds_id}_{run_ts}.json"
        payload = json.dumps(
            {"datastream_id": ds_id, "observations": observations},
            ensure_ascii=False,
            indent=2
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(payload)
        
        checksum = hashlib.sha256(payload.encode()).hexdigest()
        manifest["files"].append({
            "datastream_id":    ds_id,
            "filename":         filename,
            "record_count":     len(observations),
            "checksum_sha256":  checksum,
        })

        logger.info("Fetching observations for datastream successful", extra={
            "datastream_id": ds_id,
            "record_count": len(observations),
            "data_file": filename,
            "checksum_sha256": checksum,
            **log_context,
        })

    manifest = sign_manifest(manifest)
    if not verify_manifest(manifest, pub_key_path="config/manifest_signing.pub"):
        raise RuntimeError("Manifest signature verification failed")

    manifest_path = f"data/raw/bicycle/manifest_{run_ts}.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    
    logger.info("Fetching data successful", extra={
        "datastream_ids": datastream_ids,
        "manifest_path": manifest_path,
        **log_context,
    })


with DAG(
    dag_id="training_bicycle_data_pull",
    start_date=datetime(2026, 4, 16),
    schedule=None,
    catchup=False,
    params={
        "start_date": Param("2023-01-01", type="string"),
        "end_date":   Param("2025-12-31", type="string"),
        "layer_name": Param("Anzahl_Fahrraeder_Zaehlstelle_1-Tag", type="string"),
    }
) as dag:

    ping_task = PythonOperator(
        task_id="ping_sta_api",
        python_callable=ping_sta_api,
    )   
    
    discover_task = PythonOperator(
        task_id="discover_datastreams",
        python_callable=discover_datastreams,
    )

    extract_task = PythonOperator(
        task_id="fetch_sta_api_data",
        python_callable=fetch_sta_api_data,
    )

    ping_task >> discover_task >> extract_task
