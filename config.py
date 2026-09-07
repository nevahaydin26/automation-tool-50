import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-50",
    "debug": False,
    "max_workers": 4,
    "timeout": 30,
    "log_level": "INFO",
    "output_dir": "./output",
}


def load_config(config_path: str = None) -> Dict[str, Any]:
    """Load configuration from a JSON file, overriding default values."""
    config = DEFAULT_CONFIG.copy()

    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update(user_config)
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: Failed to load {config_path}: {err}")

    # Allow environment variable overrides (APP_KEY format)
    for key in config:
        env_var = f"APP_{key.upper()}"
        if env_var in os.environ:
            raw_val = os.environ[env_var]
            if isinstance(config[key], bool):
                config[key] = raw_val.lower() in ("true", "1", "yes")
            elif isinstance(config[key], int):
                try:
                    config[key] = int(raw_val)
                except ValueError:
                    pass
            else:
                config[key] = raw_val

    return config


def get_config_value(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely retrieve configuration keys with fallback defaults."""
    return config.get(key, default)
