import re

def validate_input(data):
    """
    Validates input structure and format for automation-tool-50.
    Returns (bool, str) tuple representing status and error message.
    """
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"

    required_fields = ['task_id', 'payload']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    if not isinstance(data['task_id'], int):
        return False, "task_id must be an integer"

    # Validate payload format using regex
    if not re.match(r'^[a-zA-Z0-9_-]+$', str(data['payload'])):
        return False, "payload contains invalid characters"

    return True, "success"

def process_loop(items):
    """
    Main processing loop with integrated input validation.
    """
    for item in items:
        is_valid, error = validate_input(item)
        if not is_valid:
            print(f"Validation failed for item: {error}")
            continue
        
        print(f"Processing task: {item['task_id']}")

if __name__ == "__main__":
    mock_data = [
        {'task_id': 1, 'payload': 'data_01'},
        {'task_id': 'invalid', 'payload': 'bad'}
    ]
    process_loop(mock_data)