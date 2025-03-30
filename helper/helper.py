import random
import time
import psutil
from typing import Optional
import subprocess

def get_processes() -> list:
    """Fetch all process names."""
    monitored = set()
    for proc in psutil.process_iter(attrs=["name"]):
        try:
            name = proc.info["name"]
            if name and "(" not in name:  # Exclude processes with parentheses in the name
                monitored.add(name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if not monitored:
        raise ValueError("Failed to find any processes.")
    return list(monitored)  # Convert set to list for further processing

def generate_and_run_command_prompt(processes: list, number_of_processes: Optional[int] = None, interval: int = 1) -> None:
    """
    Generates a command to run the monitor script and executes it.

    :param processes: List of process names to monitor.
    :param number_of_processes: The number of processes to randomly select from the list. 
                                 If None, it will monitor all processes available.
    :param interval: Time interval (in seconds) to check process status.
    """
    # Fetch all available processes
    processes = list(get_processes())
    
    # Select random processes if required
    if number_of_processes:
        processes = random.sample(processes, k=number_of_processes)

    # Join the selected processes into a string
    processes = " ".join(processes).strip()

    # Command to run the monitor script
    path_to_monitor = "monitor/monitor.py"
    command = f"python3 {path_to_monitor} -p {processes} -i {interval}"
    print(f"For manual run, copy and paste the following command: {command}")

    print(f"Start monitoring every {interval} seconds.")
    
    # Run the command as a subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
