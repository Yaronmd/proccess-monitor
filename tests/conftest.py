import pytest
import psutil
from unittest.mock import MagicMock, patch
from monitor.monitor import Monitor


@pytest.fixture
def mock_monitor():
    """Fixture to create a Monitor instance with mock process names"""
    return Monitor(process_names=["chrome", "zsh"], interval=3)


@pytest.fixture
def mock_process_list():
    """Fixture to provide a list of mocked process instances"""

    mock_proc1 = MagicMock()
    mock_proc1.info = {"name": "chrome"}
    mock_proc1.name.return_value = "chrome"
    mock_proc1.pid = 1234
    mock_proc1.is_running.return_value = True

    mock_proc2 = MagicMock()
    mock_proc2.info = {"name": "zsh"}
    mock_proc2.name.return_value = "zsh"
    mock_proc2.pid = 5678
    mock_proc2.is_running.return_value = False

    mock_proc3 = MagicMock()
    mock_proc3.info = {"name": "notepad"}
    mock_proc3.name.return_value = "notepad"
    mock_proc3.pid = 9101
    mock_proc3.is_running.return_value = True

    mock_proc4 = MagicMock()
    mock_proc4.info = {"name": "docker"}
    mock_proc4.name.return_value = "docker"
    mock_proc4.pid = 1112
    mock_proc4.is_running.return_value = False

    return [mock_proc1, mock_proc2, mock_proc3,mock_proc4]


@pytest.fixture
def mock_process_iter(mock_process_list):
    """Patch `psutil.process_iter` to return mock processes"""
    with patch("psutil.process_iter", return_value=mock_process_list):
        yield
