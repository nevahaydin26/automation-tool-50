import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file='app.log', max_bytes=1048576, backup_count=5):
    """Sets up a rotating file logger and a stream logger."""
    logger = logging.getLogger('automation_tool')
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    log = setup_logger('logs/automation.log')
    log.info('Logger initialized with rotating file handler')
