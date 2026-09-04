import os
from pathlib import Path

# Base application paths
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Ensure required directories exist
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Operational configuration
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5

# Supported file extensions for automation tasks
SUPPORTED_EXTENSIONS = {".json", ".csv", ".yaml", ".txt"}

# Environment specific configurations
ENV = os.getenv("APP_ENV", "development")
DEBUG_MODE = ENV == "development"

# Header definitions for standardized outputs
REQUEST_HEADERS = {
    "User-Agent": "automation-tool-50/1.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_timeout_setting(multiplier: int = 1) -> int:
    """Calculates timeout based on environment settings."""
    return DEFAULT_TIMEOUT * multiplier