"""decompile_cli.py

This script provides a command line interface for decompiling binaries using
Ghidra.

The script defines a function to decompile a specified binary file using
Ghidra's headless analyzer. It constructs and executes the necessary command,
capturing and printing the output for debugging purposes. The script is
intended to be run directly from the command line, with arguments specifying
the paths of the binary file and the output file.
"""

import subprocess
import os
import argparse

# Modify this to your Ghidra installation path
GHIDRA_PATH = "/path/to/ghidra_10.3.2_PUBLIC"
GHIDRA_SCRIPT_PATH = "../java/ExportDecompiledCode.java"


def decompile_binary(binary_path, output_path):
    """
    Decompile the specified binary using Ghidra's headless analyzer.

    This function constructs the command required to run Ghidra's headless
    analyzer, specifying the binary to be decompiled and the path to save the
    decompiled output. It then executes the command, capturing and printing the
    standard output and standard error for debugging purposes. The Ghidra
    script specified by `GHIDRA_SCRIPT_PATH` is used to perform the
    decompilation.

    Args:
        binary_path (str): The file path of the binary to be decompiled.
        output_path (str): The file path where the decompiled output will be saved.
    """
    # Construct the command for Ghidra's headless analyzer
    cmd = [
        os.path.join(GHIDRA_PATH, "support", "analyzeHeadless"),
        ".",  # Project directory (you can customize this)
        "TempProject",  # Temporary project name (you can customize this)
        "-import",
        binary_path,
        "-postScript",
        GHIDRA_SCRIPT_PATH,
        output_path,  # This will be passed as an argument to the Ghidra script
        "-deleteProject",  # Delete the temporary project after analysis
    ]

    # Execute the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Print Ghidra's output (for debugging purposes, can be omitted)
    print(stdout.decode())
    print(stderr.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompile binary using Ghidra")
    parser.add_argument("binary_path", help="Path to the binary to be decompiled")
    parser.add_argument("output_path", help="Path to save the decompiled output")
    args = parser.parse_args()

    decompile_binary(args.binary_path, args.output_path)
