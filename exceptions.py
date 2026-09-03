from typing import Optional

class AutomationError(Exception):
    """Base exception class for automation-tool-50."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(AutomationError):
    """Raised when the tool configuration is invalid or missing."""
    pass

class ExecutionError(AutomationError):
    """Raised when an automation task fails during execution."""
    def __init__(self, message: str, task_id: Optional[str] = None) -> None:
        super().__init__(message)
        self.task_id = task_id

class ValidationError(AutomationError):
    """Raised when input data does not meet schema requirements."""
    pass

class ConnectionError(AutomationError):
    """Raised when external service connectivity is lost."""
    pass