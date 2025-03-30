import pytest
from monitor.monitor import Monitor
from rich.console import Console

def test_get_initial_processes(mock_monitor, mock_process_iter, mock_process_list):
    """Test if the Monitor correctly filters processes by name"""

    result = mock_monitor.get_initial_processes()

    # Only chrome and zsh should be returned
    assert len(result) == 2
    assert any(proc.info["name"] == "chrome" for proc in result)
    assert any(proc.info["name"] == "zsh" for proc in result)
    assert all(proc.info["name"] != "notepad" for proc in result)


def test_generate_dashboard(mock_monitor, mock_process_list):
    """Test if the dashboard table is generated correctly"""

    mock_monitor.monitored_processes = mock_process_list
    # Generate the dashboard panel
    panel = mock_monitor.generate_dashboard()

    # Create a Console instance with record=True
    console = Console(record=True)

    # Render the panel and capture the output
    console.print(panel)

    # Export the text from the recorded console output
    rendered_text = console.export_text(clear=True, styles=False)

    # Assertions
    assert "Process Name" in rendered_text and "PID" in rendered_text and "Status" in rendered_text
    assert "chrome" in rendered_text
    assert "1234" in rendered_text
    assert "Running" in rendered_text
    assert "Stopped" in rendered_text 

def test_monitor_initialization():
    """Test that the Monitor class initializes correctly with given process names and interval."""
    monitor = Monitor(process_names=["zsh"], interval=1)

    assert isinstance(monitor, Monitor)
    assert monitor.process_names == {"zsh"}
    assert monitor.interval == 1
    assert isinstance(monitor.monitored_processes, list)


def test_invalid_process_names():
    """Test how the Monitor class handles non-existing or invalid process names."""
    assert ValueError , Monitor(process_names=["123"], interval=1)
    assert ValueError , Monitor(process_names=[""], interval=1)
    
def test_dashboard_refresh(mock_process_list,mock_process_iter):
    """Test that the dashboard updates correctly when process statuses change.
    inital mock with status, change the status and validate
    """

    monitor = Monitor(process_names=["chrome", "VS code"], interval=1)
    monitor.console = Console(record=True)

    mock_process_list[0].name.return_value = "chrome"
    mock_process_list[1].name.return_value = "VS code"

    mock_process_list[0].is_running.return_value = True  
    mock_process_list[1].is_running.return_value = False  
    monitor.monitored_processes = mock_process_list[:2]

    # Capture initial dashboard output
    monitor.console.print(monitor.generate_dashboard())
    initial_rendered_text = monitor.console.export_text(clear=True)

    # Change process status "VS code" to "Running"
    mock_process_list[1].is_running.return_value = True  

    # Capture updated dashboard output
    monitor.console.print(monitor.generate_dashboard())
    updated_rendered_text = monitor.console.export_text(clear=True)

    assert "Stopped" in initial_rendered_text  # Validate "VS code" state == "Stopped"
    assert "Running" in updated_rendered_text  # Validate "VS code" state changed to "Running"
    assert initial_rendered_text != updated_rendered_text  # Ensure output changes

    



    