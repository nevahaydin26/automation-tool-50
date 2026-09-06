import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively strips whitespace from string values in dictionary."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def load_json_file(file_path: str) -> Optional[Dict]:
    """Safely loads and parses JSON configuration files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return clean_data(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return None

def validate_keys(data: Dict, required: list) -> bool:
    """Checks if all required keys exist in dictionary."""
    return all(key in data for key in required)

if __name__ == '__main__':
    # Example usage for testing structure
    test_input = {"name": "  dev  ", "settings": ["  on  ", "  auto  "]}
    print(clean_data(test_input))