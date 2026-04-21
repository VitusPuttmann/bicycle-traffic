from airflow.config_templates.airflow_local_settings import DEFAULT_LOGGING_CONFIG
import copy

LOG_CONFIG = copy.deepcopy(DEFAULT_LOGGING_CONFIG)

LOG_CONFIG["formatters"]["json"] = {
    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
    "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
}

LOG_CONFIG["handlers"]["json_file"] = {
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "/opt/airflow/logs/dag_runs.jsonl",
    "formatter": "json",
    "maxBytes": 10_000_000,
    "backupCount": 10,
}

LOG_CONFIG["loggers"]["dags"] = {
    "handlers": ["json_file"],
    "level": "DEBUG",
    "propagate": True,
}