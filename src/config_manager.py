"""config_manager.py

Module for managing configuration settings related to Ghidra path and output
directory.

This module defines two functions to handle the reading and writing of
configuration settings to a configuration file. The settings include the file
path to the Ghidra installation and the directory path for output. The
configuration file is assumed to be located at "../conf/main.conf" relative to
this script.

The `get_config` function reads the settings from the configuration file, and
the `save_config` function writes new settings to the configuration file.

Returns:
    None: The functions are designed to be called for their side-effects
    (reading from or writing to a file), and do not return values beyond what
    is necessary for their operation.
"""

import os

CONFIG_FILE = "../conf/main.conf"

def get_config():
    """
    Get the Ghidra path and output directory from the configuration file.

    _extended_summary_
    This function checks if the configuration file exists. If it does, it reads
    the file, expecting the Ghidra path on the first line and the output
    directory on the second line. It returns these paths as a tuple. If the
    file does not exist or is improperly formatted, it returns a tuple of None
    values.

    Returns:
        tuple: A tuple containing two strings, the Ghidra path and the output
        directory, or None values if the configuration file does not exist or
        is improperly formatted.
    """
    if os.path.exists(CONFIG_FILE):
        with open(file=CONFIG_FILE, mode="r", encoding='utf-8') as f:
            lines = f.readlines()
            return lines[0].strip(), lines[1].strip()
    return None, None


def save_config(ghidra_path, output_dir):
    """
    Save the Ghidra path and output directory to the configuration file.

    This function opens the configuration file for writing (or creates it if it
    doesn't exist) and writes the Ghidra path on the first line and the output
    directory on the second line.

    Args:
        ghidra_path (str): The file path to the Ghidra installation to be saved
        to the configuration file.
        output_dir (str): The directory path where output files should be
        saved, to be saved to the configuration file.
    """
    with open(file=CONFIG_FILE, mode="w", encoding="utf-8") as f:
        f.write(ghidra_path + "\n")
        f.write(output_dir + "\n")
