import logging
import os
import sys

def get_logger(name: str):
    """Configures and returns a logger instance with error handling."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        try:
            log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
            logger.setLevel(log_level)
            
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except (ValueError, OSError) as e:
            # Fallback to stderr if stream configuration fails
            sys.stderr.write(f"Logging initialization failure: {e}\n")
            logging.basicConfig(level=logging.ERROR)
    return logger

def safe_log(logger, message: str, level: str = 'info'):
    """Utility to log messages with structural edge case handling."""
    try:
        if not isinstance(message, str):
            message = str(message)
        
        log_func = getattr(logger, level.lower(), logger.info)
        log_func(message)
    except Exception as e:
        # Prevents logging failures from crashing the main automation flow
        sys.stderr.write(f"Critical logging failure: {e}\n")