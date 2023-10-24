import pytest
from unittest.mock import patch, Mock
import decompile_cli

def test_decompile_binary():
    # Mock subprocess.Popen to avoid calling Ghidra's headless analyzer
    mock_popen = Mock()
    mock_popen.communicate.return_value = (b"Mock stdout", b"Mock stderr")
    with patch("subprocess.Popen", return_value=mock_popen) as mock_subprocess:
        decompile_cli.decompile_binary("/path/to/binary", "/path/to/output")

        # Verify that subprocess.Popen was called with the expected command
        mock_subprocess.assert_called_once_with(
            [
                "/path/to/ghidra_10.3.2_PUBLIC/support/analyzeHeadless",
                ".",
                "TempProject",
                "-import",
                "/path/to/binary",
                "-postScript",
                "../java/ExportDecompiledCode.java",
                "/path/to/output",
                "-deleteProject"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

def test_main(monkeypatch):
    # Mock argparse arguments
    mock_args = Mock(binary_path="/path/to/binary", output_path="/path/to/output")
    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda x: mock_args)

    # Mock decompile_binary function to avoid actual decompilation
    with patch("decompile_cli.decompile_binary") as mock_decompile:
        decompile_cli.main()

        # Verify that decompile_binary was called with the expected arguments
        mock_decompile.assert_called_once_with("/path/to/binary", "/path/to/output")
