import argparse
import time
from datetime import datetime
import psutil
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

class Monitor():

    def __init__(self, process_names: list, interval: int=3):
        """
        :param process_names: List of process names to monitor.
        :param interval: Time interval (in seconds) to check their status.
        """
        if interval <=0:
            raise ValueError("intrval must be greather then 0")
        self.process_names = set(process_names)
        self.interval = interval
        self.monitored_processes = self.get_initial_processes()
        self.console = Console(force_terminal=True, color_system="truecolor",record=True)

    def get_initial_processes(self) -> list:
        """Fetch all running processes and filter the required ones."""
        monitored = []
        for proc in psutil.process_iter(attrs=["name"]):
            try:
                if proc.info["name"] in self.process_names:
                    monitored.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        if not monitored:
            raise ValueError(f"Failed to find any process for {self.process_names}")
        return monitored

    def generate_dashboard(self) -> Panel:
        """Generate dashboard with process information."""
        table = Table(show_header=True, header_style="bold cyan",
                      title=f"Process Monitor {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}")
        table.add_column("Process Name", style="bold yellow")
        table.add_column("PID", style="bold magenta")
        table.add_column("Status",style="bold magenta")
        table.add_column("Started",style="bold magenta")

        for process in self.monitored_processes:
            try:
                status_text = Text(" Running ", style="bold green") if process.is_running() else Text(" Stopped ", style="bold red")
                start_time = process.create_time()
                formatted_start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
                table.add_row(Text(process.name(), style="cyan"), str(process.pid), status_text,formatted_start_time)
            except psutil.NoSuchProcess:
                continue

        return Panel(table, border_style="bright_blue")

    def start_monitoring(self):
        """Validate processes at the given interval."""
        with Live(self.generate_dashboard(), 
                  refresh_per_second=2,  # Adjust refresh rate
                  console=self.console) as live:
            try:
                while True:
                    live.update(self.generate_dashboard())  # Update the content
                    time.sleep(self.interval)  # Wait before the next refresh
            except KeyboardInterrupt:
                print("Monitoring stopped.")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Monitor with Console UI")
    parser.add_argument("-p", "--processes", nargs="+", required=True, help="List of process names to monitor")
    parser.add_argument("-i", "--interval", type=int, default=3, help="Interval in seconds (default: 3s)")
    args = parser.parse_args()

    monitor = Monitor(args.processes, args.interval)
    monitor.start_monitoring()
