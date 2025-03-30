# Process Monitor

A Python-based process monitoring tool that allows users to track system processes, display their status in real-time, and run automated tests using Pytest and Allure.

## Features
- Monitors specific processes on the system.
- Displays process status updates dynamically using `rich`.
- Supports interval-based monitoring.
- Generates test reports using `pytest` and `allure`.

## Installation

### 1. Clone the Repository
```sh 
cd process-monitor
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage


### 1. Execute `app.py`

The `app.py` script is the **main entry point** for the project. It automates process monitoring by dynamically selecting processes and running the `monitor.py` script.

### 🔹 **What `app.py` Does:**
- **Fetches Running Processes** – Retrieves all active process names.
- **Random Process Selection** *(Optional)* – Can randomly select a subset of processes if specified.
- **Generates a Monitoring Command** – Constructs the command to execute `monitor.py`.
- **Runs Monitoring Automatically** – Executes the command using `subprocess.run()`.

This simplifies process monitoring compared to manually running `monitor.py`.

```sh
python3 app.py
```

### 2. Run the Monitoring Script
```sh
python3 monitor/monitor.py -p process_name1 process_name2 -i 3
```
- `-p`: List of process names to monitor.
- `-i`: Time interval in seconds (default is `3`).

Example:
```sh
python3 monitor/monitor.py -p python chrome -i 5
```



## Running Tests

### 1. Run Pytest
```sh
pytest -s
```

### 2. Generate Allure Report
```sh
pytest -s --alluredir=allure-results
```

### 3. View Allure Report
```sh
allure serve allure-results
```

## Error Handling
- If no processes are found, ensure the process names are correct.
- Use `ps aux` (Linux/macOS) or `tasklist` (Windows) to list running processes.
- If `allure` is not recognized, install it using:
  ```sh
  npm install -g allure-commandline
  ```

## License
MIT License. See `LICENSE` for details.

