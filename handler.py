import functools
import time
import logging

# Configure logger for automation-tool-50
logger = logging.getLogger(__name__)

# Cache for repetitive compute tasks
_memo_cache = {}

def memoize(func):
    """Decorator to cache results of expensive operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memo_cache:
            _memo_cache[key] = func(*args, **kwargs)
        return _memo_cache[key]
    return wrapper

class DataHandler:
    """Efficient processing of core data payloads."""
    
    def __init__(self, threshold=1000):
        self.threshold = threshold

    @memoize
    def transform(self, data: list) -> list:
        """Apply complex transformations with caching."""
        if len(data) > self.threshold:
            logger.warning("High volume payload detected: %d records", len(data))
        
        # Use list comprehension for performance
        return [item * 2 for item in data if isinstance(item, (int, float))]

def process_batch(items: list):
    """Execution entry point for batches."""
    handler = DataHandler()
    start_time = time.perf_counter()
    
    result = handler.transform(tuple(items))
    
    duration = time.perf_counter() - start_time
    logger.info("batch processing completed in %.4f seconds", duration)
    return result