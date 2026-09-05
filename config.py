import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

def load_configuration(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads JSON config with fallback to default settings."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as file:
                user_config = json.load(file)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config {config_path}: {e}")
    
    return config

def save_configuration(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists current dictionary configuration to disk."""
    try:
        with open(config_path, "w") as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        print(f"Error: Failed to save config to {config_path}: {e}")