import time
from typing import List, Dict, Any

class TaskHandler:
    """Handler for general automation tasks."""

    def __init__(self, max_retries: int = 3) -> None:
        """Initialize with max retries."""
        self.max_retries: int = max_retries
        self.tasks: List[Dict[str, Any]] = []
        self.completed: int = 0

    def add_task(self, task: Dict[str, Any]) -> None:
        """Add task to queue. Task needs 'type' and 'data'."""
        if 'type' not in task or 'data' not in task:
            raise ValueError("Task must have 'type' and 'data'")
        self.tasks.append(task)

    def execute_task(self, task: Dict[str, Any]) -> bool:
        """Execute task, return success."""
        task_type: str = task.get('type', '')
        data: Any = task.get('data')
        for attempt in range(self.max_retries):
            try:
                if task_type == 'print':
                    print(f"Printing: {data}")
                    time.sleep(0.1)
                    return True
                elif task_type == 'wait':
                    wait_time: float = float(data) if data else 1.0
                    time.sleep(wait_time)
                    return True
                else:
                    print(f"Unknown task type: {task_type}")
                    return False
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == self.max_retries - 1:
                    return False
        return False

    def run_all(self) -> int:
        """Run all tasks and return count of successes."""
        success_count: int = 0
        for task in self.tasks:
            if self.execute_task(task):
                success_count += 1
                self.completed += 1
        return success_count

    def get_stats(self) -> Dict[str, int]:
        """Return stats dict."""
        return {
            'total_tasks': len(self.tasks),
            'completed': self.completed,
            'pending': len(self.tasks) - self.completed
        }

if __name__ == "__main__":
    handler = TaskHandler(max_retries=2)
    handler.add_task({'type': 'print', 'data': 'Starting automation'})
    handler.add_task({'type': 'wait', 'data': '0.5'})
    handler.add_task({'type': 'print', 'data': 'Automation complete'})
    completed = handler.run_all()
    stats = handler.get_stats()
    print(f"Completed {completed} tasks")
    print(f"Stats: {stats}")