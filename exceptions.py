class AutomationError(Exception):
    """Base exception for all automation-tool-50 errors."""
    pass

class ConfigurationError(AutomationError):
    """Raised when configuration validation fails."""
    pass

class ExecutionError(AutomationError):
    """Raised when a process fails during execution."""
    pass

class TimeoutError(AutomationError):
    """Raised when an operation exceeds time limits."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Helper to enforce non-null values."""
    if value is None:
        raise ValueError(message)
    return value

def validate_path(path):
    """Helper to ensure file paths are provided."""
    if not path or not isinstance(path, str):
        raise ConfigurationError(f"Invalid path provided: {path}")
    return path

def handle_execution_error(func):
    """Decorator for wrapping operations with custom error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise ExecutionError(f"Operation failed: {str(e)}") from e
    return wrapper