"""config_manager.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os

CONFIG_FILE = "../conf/main.conf"


def get_config():
    """
    Get the Ghidra path and output directory from the configuration file.

    _extended_summary_

    Return as a tuple (ghidra_path, output_dir).
    Returns:
        _type_: _description_
    """
    if os.path.exists(CONFIG_FILE):
        with open(file=CONFIG_FILE, mode="r", encoding='utf-8') as f:
            lines = f.readlines()
            return lines[0].strip(), lines[1].strip()
    return None, None


def save_config(ghidra_path, output_dir):
    """
    Save the Ghidra path and output directory to the configuration file.

    _extended_summary_

    Args:
        ghidra_path (_type_): _description_
        output_dir (_type_): _description_
    """
    with open(file=CONFIG_FILE, mode="w", encoding="utf-8") as f:
        f.write(ghidra_path + "\n")
        f.write(output_dir + "\n")
