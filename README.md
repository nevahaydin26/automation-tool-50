# automation-tool-50

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

automation-tool-50 is a Python command-line tool for running configurable automation workflows. It handles repetitive tasks such as file operations, data movement, and external API calls through simple definitions.

## Features

- Define workflows in YAML with sequential steps and basic error handling
- Built-in actions for moving files, making HTTP requests, and running Python code
- Time-based scheduling using cron expressions
- Structured logging with optional failure alerts

## Installation

```bash
git clone https://github.com/Developer/automation-tool-50.git
cd automation-tool-50
pip install -r requirements.txt
```

## Usage

Create a workflow file and execute it:

```bash
automation-tool-50 run workflow.yaml
```

Example `workflow.yaml`:

```yaml
name: organize-downloads
steps:
  - action: move_files
    source: "~/Downloads/*.pdf"
    destination: "~/Documents/PDFs/"
  - action: http_request
    url: "https://api.example.com/notify"
    method: POST
```

## License

This project is licensed under the MIT License.