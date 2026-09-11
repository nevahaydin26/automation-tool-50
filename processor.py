import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class BatchProcessor:
    """Processor class for validating and executing incoming task payloads."""

    def __init__(self, required_fields: List[str] = None):
        self.required_fields = required_fields or ["task_id", "action", "payload"]
        self.processed_count = 0
        self.failed_count = 0

    def validate_input(self, item: Dict[str, Any]) -> bool:
        """Validate single item dictionary against structural requirements."""
        if not isinstance(item, dict):
            logging.warning("Invalid input type: Expected dictionary payload")
            return False

        for field in self.required_fields:
            if field not in item:
                logging.warning(f"Validation error: Missing required field '{field}'")
                return False

        if not isinstance(item["task_id"], (int, str)) or not str(item["task_id"]).strip():
            logging.warning("Validation error: 'task_id' must be a non-empty string or integer")
            return False

        if not isinstance(item["payload"], dict):
            logging.warning(f"Validation error for task '{item['task_id']}': 'payload' must be a dict")
            return False

        return True

    def process_queue(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop with strict input validation for task items."""
        results = []

        for index, item in enumerate(items):
            # Perform input validation check before attempting task execution
            if not self.validate_input(item):
                logging.error(f"Skipping invalid item at queue position {index}")
                self.failed_count += 1
                continue

            try:
                task_id = item["task_id"]
                action = item["action"]
                payload = item["payload"]

                # Execute payload processing
                summary = f"Action '{action}' executed with {len(payload)} parameters"
                results.append({"task_id": task_id, "status": "completed", "result": summary})
                
                self.processed_count += 1
                logging.info(f"Successfully processed task '{task_id}'")
            except Exception as err:
                logging.error(f"Unhandled failure during processing of task '{item.get('task_id')}': {err}")
                self.failed_count += 1

        return results
