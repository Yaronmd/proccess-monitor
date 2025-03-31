# Process Monitor

A Python-based process monitoring tool that allows users to track system processes, display their status in real-time, including automated unitesting with allure report.

## Features
- Monitors specific processes on the system.
- Displays process status updates dynamically using `rich`.
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


###  **What `app.py` Does:**
- **Fetches Running Processes** – Retrieves all active process names.
- **Random Process Selection** *(Optional)* – Can randomly select a subset of processes if specified.
- **Generates a Monitoring Command** – Constructs the command to execute `monitor.py`.
- **Runs Monitoring Automatically** – Executes the command using `subprocess`.

This simplifies process monitoring compared to manually running `monitor.py`.

```sh
python3 app.py
```
See app.py for example usages, including how to run and monitor specific or random processes.

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

## Description of Key Directories and Files:

- **`app.py`**: Main script for generating and running process monitoring commands.
- **`monitor/`**: Contains the `monitor.py` script as a module.
- **`tests/`**: Includes unit tests for your monitoring system.
- **`test_example.py`**: Example test case to demonstrate how tests are structured.
  - **`test_monitor.py`**: Contains unit tests to validate the functionality of the `monitor.py` script. This test case can verify if the script correctly executes the monitoring process and handles any errors.
  - **`conftest.py`**: file is used to define fixtures, mock data.
- **`allure-results/`**: Directory that stores results from tests executed with Allure integration.


## Error Handling
- If no processes are found, ensure the process names are correct.
- Use `ps aux` (Linux/macOS) or `tasklist` (Windows) to list running processes.
- If `allure` is not recognized, install it using:
  ```sh
  npm install -g allure-commandline
  ```

## License
MIT License. See `LICENSE` for details.

