class AutomationError(Exception):
    """Base exception class for the automation tool."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ValidationError(AutomationError):
    """Raised when input validation fails in the processing loop."""
    def __init__(self, message: str, field: str = None, value: str = None):
        super().__init__(message)
        self.field = field
        self.value = value

    def __str__(self) -> str:
        if self.field:
            return f"Validation failed for field '{self.field}' [value: {self.value}]: {self.message}"
        return f"Validation failed: {self.message}"


class MissingRequiredFieldError(ValidationError):
    """Raised when a required config or input field is missing."""
    def __init__(self, field: str):
        super().__init__("Field is required but was not found.", field=field)


class InvalidFormatError(ValidationError):
    """Raised when an input field value does not match the required format."""
    def __init__(self, field: str, value: str, expected: str):
        super().__init__(
            f"Expected format: {expected}",
            field=field,
            value=value
        )
