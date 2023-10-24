import pytest
from unittest.mock import patch, mock_open
import install

def test_find_ghidra_installation_found():
    with patch("os.path.exists", return_value=True):
        assert install.find_ghidra_installation() in install.STANDARD_LOCATIONS

def test_find_ghidra_installation_not_found():
    with patch("os.path.exists", return_value=False):
        assert install.find_ghidra_installation() is None

def test_get_ghidra_path_from_config():
    mock_data = "/path/to/ghidra\n"
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        ghidra_path = install.get_ghidra_path_from_config()
        assert ghidra_path == "/path/to/ghidra"

def test_save_ghidra_path_to_config():
    m = mock_open()
    with patch("builtins.open", m):
        install.save_ghidra_path_to_config("/path/to/ghidra")
    m.assert_called_once_with("./conf/main.conf", mode="w", encoding="utf-8")

def test_main_config_exists():
    with patch("install.get_ghidra_path_from_config", return_value="/path/to/ghidra"):
        with patch("builtins.print") as mock_print:
            install.main()
            mock_print.assert_called_once_with("Using Ghidra installation at: /path/to/ghidra")

def test_main_config_not_exists_but_found_in_standard_locations():
    with patch("install.get_ghidra_path_from_config", return_value=None):
        with patch("install.find_ghidra_installation", return_value="/standard/path/to/ghidra"):
            with patch("builtins.print") as mock_print:
                install.main()
                mock_print.assert_called_once_with("Using Ghidra installation at: /standard/path/to/ghidra")

def test_main_user_input_required():
    with patch("install.get_ghidra_path_from_config", return_value=None):
        with patch("install.find_ghidra_installation", return_value=None):
            with patch("builtins.input", return_value="/user/input/path/to/ghidra"):
                with patch("builtins.print") as mock_print:
                    install.main()
                    mock_print.assert_called_once_with("Using Ghidra installation at: /user/input/path/to/ghidra")
