import os
import json
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def load_json(file_path: str) -> Optional[dict]:
    """Load and parse JSON from a file system path."""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"failed to read json from {file_path}: {e}")
    return None

def save_json(data: Any, file_path: str) -> bool:
    """Serialize data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            return True
    except IOError as e:
        logger.error(f"failed to write json to {file_path}: {e}")
        return False

def ensure_directory(dir_path: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

def sanitize_filename(name: str) -> str:
    """Remove characters unsafe for filesystem paths."""
    keep = (' ', '.', '_')
    return "".join(c for c in name if c.isalnum() or c in keep).strip()