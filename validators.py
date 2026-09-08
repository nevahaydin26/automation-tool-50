import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify email address format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_numeric(value: Any, min_val: Optional[int] = None, max_val: Optional[int] = None) -> bool:
    """Check if value is numeric and within optional range."""
    if not isinstance(value, (int, float)):
        return False
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

def validate_non_empty_string(value: Any) -> bool:
    """Ensure input is a string and not blank."""
    return isinstance(value, str) and len(value.strip()) > 0

def sanitize_input(value: str) -> str:
    """Strip whitespace and prevent common injection artifacts."""
    if not isinstance(value, str):
        return ""
    return value.strip().replace(';', '').replace('--', '')