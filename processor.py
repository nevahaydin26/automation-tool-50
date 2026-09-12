import os
import json
import logging
from typing import Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json_file(file_path: str) -> dict:
    """Loads and parses a JSON file from disk."""
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return {}
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error reading {file_path}: {e}")
        return {}

def ensure_directory(path: str) -> None:
    """Creates directory structure if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory: {path}")

def format_data_payload(data: Any, prefix: str = "ID_") -> str:
    """Converts object to string with specified prefix."""
    try:
        return f"{prefix}{str(data).strip()}"
    except Exception as e:
        logger.warning(f"Formatting error: {e}")
        return f"{prefix}UNKNOWN"

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.getenv(key, default) or ""