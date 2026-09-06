# automation-tool-50

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, Python-based automation engine designed to streamline repetitive local tasks like directory cleaning, batch file renaming, and API synchronization. It offers a clean CLI interface and robust yaml configuration options, making it easy for developers to orchestrate complex workflows with minimal overhead.

## Key Features

*   **Smart File Watchers:** Monitor specified directories in real-time and trigger custom Python functions instantly upon file generation or modification.
*   **Flexible Task Scheduler:** Schedule recurring operations using standard cron syntax directly inside your configuration files, bypassing platform-specific schedulers.
*   **Rich Console Reporting:** Gain deep visibility with colorized terminal logs, structured JSON execution histories, and automated email alerts on task failures.

## Installation

Clone the repository and install the package using `pip`:

```bash
git clone https://github.com/Developer/automation-tool-50.git
cd automation-tool-50
pip install -r requirements.txt
pip install .
```

## Quick Start

Define your tasks in a `tasks.yaml` file, then execute them programmatically:

```python
from automation_tool_50 import TaskRunner

# Initialize the runner with your configuration file
runner = TaskRunner(config_path="tasks.yaml")

# Execute a specific workflow
runner.run_task("archive_old_logs")
```

To run tasks directly from the command line:

```bash
auto50 run archive_old_logs --config tasks.yaml
```