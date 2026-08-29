import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(
    name: str = "automation_tool_50",
    log_file: str = "logs/automation.log",
    level: int = logging.INFO,
    max_bytes: int = 10 * 1024 * 1024,  # 10 MB
    backup_count: int = 5,
) -> logging.Logger:
    """Configure and return a logger with rotating file handler.

    Creates log directory if it does not exist.

    Prevents duplicate handlers on repeated calls.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure log directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Rotating file handler
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)

    # Console handler for output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Standard formatter
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers only if not already present
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Quick test when run directly
if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
