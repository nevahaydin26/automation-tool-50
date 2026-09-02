import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-50",
    "max_retries": 3,
    "timeout_seconds": 60,
    "log_level": "INFO",
    "output_directory": "./output",
    "debug_mode": False,
    "batch_size": 10,
}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration merging file values over defaults.
    Supports environment variable overrides for keys prefixed with AUTO_.
    """
    config = DEFAULT_CONFIG.copy()
    if config_path is None:
        config_path = "config.json"
    path = Path(config_path)
    if path.is_file():
        try:
            with open(path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
            if isinstance(file_config, dict):
                config.update(file_config)
        except (json.JSONDecodeError, OSError) as exc:
            # Log warning but continue with defaults
            print(f"Config load warning for {config_path}: {exc}")
    # Apply environment overrides
    for key, default_value in DEFAULT_CONFIG.items():
        env_var = f"AUTO_{key.upper()}"
        if env_var in os.environ:
            env_value = os.environ[env_var]
            if isinstance(default_value, bool):
                config[key] = env_value.lower() in ("true", "1", "yes", "on")
            elif isinstance(default_value, int):
                try:
                    config[key] = int(env_value)
                except ValueError:
                    config[key] = default_value
            else:
                config[key] = env_value
    return config

class ConfigLoader:
    """Simple configuration loader class for easy access."""
    def __init__(self, config_path: Optional[str] = None):
        self._config = load_config(config_path)
    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value with optional default."""
        return self._config.get(key, default)
    def get_all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""
        return self._config.copy()
    def __getitem__(self, key: str) -> Any:
        if key not in self._config:
            raise KeyError(f"Config key not found: {key}")
        return self._config[key]

# Example usage (not executed here)
# config = ConfigLoader()
# print(config.get("timeout_seconds"))