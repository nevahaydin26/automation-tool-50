import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name="automation_tool", log_file="logs/app.log", level=logging.INFO, max_bytes=5242880, backup_count=5):
    """Setup logger with rotating file handler and console output."""
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setLevel(level)
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

# Example of using the logger
if __name__ == "__main__":
    log = setup_logger()
    log.debug("This is a debug message")
    log.info("Logger setup complete")
    log.warning("Sample warning")
    log.error("Sample error message")
    # Log multiple times to demonstrate
    for i in range(20):
        log.info(f"Test log entry {i + 1}")
