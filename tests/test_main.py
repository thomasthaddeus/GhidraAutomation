import pytest
from unittest.mock import patch, mock_open
from main import find_ghidra_installation, get_config, save_config

def test_find_ghidra_installation_found():
    with patch("os.path.exists", return_value=True):
        assert find_ghidra_installation() in ["/usr/bin/ghidra", "/usr/local/bin/ghidra", "/opt/ghidra"]

def test_find_ghidra_installation_not_found():
    with patch("os.path.exists", return_value=False):
        assert find_ghidra_installation() is None

def test_get_config():
    mock_data = "/path/to/ghidra\n/path/to/output\n"
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        ghidra_path, output_dir = get_config()
        assert ghidra_path == "/path/to/ghidra"
        assert output_dir == "/path/to/output"

def test_save_config():
    m = mock_open()
    with patch("builtins.open", m):
        save_config("/path/to/ghidra", "/path/to/output")
    m.assert_called_once_with("../conf/main.conf", mode="w", encoding="utf-8")
