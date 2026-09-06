import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from typing import List, Dict, Any, Callable


class WorkflowEngine:
    """Core workflow execution engine with optimized parallel task processing."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._executor = ThreadPoolExecutor(max_workers=self.max_workers)

    @staticmethod
    @lru_cache(maxsize=256)
    def _compile_template(template: str, kwargs_tuple: tuple) -> str:
        """Cached template compiler for recurring automation text transformations."""
        result = template
        for key, val in kwargs_tuple:
            result = result.replace(f"{{{key}}}", str(val))
        return result

    def render_payload(self, template: str, params: Dict[str, Any]) -> str:
        """Renders a payload template using cached compilation logic."""
        kwargs_tuple = tuple(sorted(params.items()))
        return self._compile_template(template, kwargs_tuple)

    def process_batch(self, task_fn: Callable[[Any], Any], items: List[Any]) -> List[Any]:
        """Executes a batch of automation tasks concurrently using thread pooling."""
        results = [None] * len(items)
        future_to_index = {
            self._executor.submit(task_fn, item): i
            for i, item in enumerate(items)
        }

        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                results[index] = future.result()
            except Exception as exc:
                results[index] = {"error": str(exc), "status": "failed"}

        return results

    def shutdown(self) -> None:
        """Cleanly releases worker thread resources."""
        self._executor.shutdown(wait=True)
