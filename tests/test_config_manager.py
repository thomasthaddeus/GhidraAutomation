
import pytest
from unittest.mock import patch, mock_open
from config_manager import find_ghidra_installation, get_ghidra_path_from_config, save_ghidra_path_to_config
from src.logger import test_logger

def test_find_ghidra_installation_found_in_config_manager():
    with patch("os.path.exists", return_value=True):
        assert find_ghidra_installation() in ["/usr/bin/ghidra", "/usr/local/bin/ghidra", "/opt/ghidra"]

def test_find_ghidra_installation_not_found_in_config_manager():
    with patch("os.path.exists", return_value=False):
        assert find_ghidra_installation() is None

def test_get_ghidra_path_from_config():
    mock_data = "/path/to/ghidra\n"
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        ghidra_path = get_ghidra_path_from_config()
        assert ghidra_path == "/path/to/ghidra"

def test_save_ghidra_path_to_config():
    m = mock_open()
    with patch("builtins.open", m):
        save_ghidra_path_to_config("/path/to/ghidra")
    m.assert_called_once_with("./conf/main.conf", mode="w", encoding="utf-8")
