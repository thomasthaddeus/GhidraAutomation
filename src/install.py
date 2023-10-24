"""install.py

This script facilitates the detection and configuration of Ghidra installation
path.

The script provides functions to automatically find the Ghidra installation
directory from a set of standard locations, retrieve the Ghidra path from a
configuration file, or save a specified Ghidra path to a configuration file.
The main function orchestrates these tasks to ensure that the Ghidra path is
properly configured before proceeding with further analysis tasks.

Returns:
    None: This script is intended to be run as a standalone utility, and does
    not return any values when executed.
"""

import os

GHIDRA_SCRIPT = "support/analyzeHeadless"

# List of standard locations to check for Ghidra installation
STANDARD_LOCATIONS = [
    "/usr/bin/ghidra",
    "/usr/local/bin/ghidra",
    "/opt/ghidra"
]

def find_ghidra_installation():
    """
    Try to find the Ghidra installation directory by checking standard
    locations.

    This function iterates through a predefined list of standard file paths
    where Ghidra might be installed. It checks whether the `GHIDRA_SCRIPT`
    exists in any of these locations, and returns the directory path if found.

    Returns:
        str or None: The file path of the Ghidra installation directory if
        found, otherwise None.
    """
    for location in STANDARD_LOCATIONS:
        if os.path.exists(os.path.join(location, GHIDRA_SCRIPT)):
            return location
    return None

def get_ghidra_path_from_config():
    """
    Try to get the Ghidra path from the configuration file.

    This function checks for the existence of a configuration file and reads
    the Ghidra path from it if present.

    Returns:
        str or None: The Ghidra path as a string if found in the configuration
        file, otherwise None.
    """
    if os.path.exists("./conf/main.conf"):
        with open("./conf/main.conf", mode='r', encoding='utf-8') as f:
            return f.readline().strip()
    return None

def save_ghidra_path_to_config(path):
    """
    Save the Ghidra path to the configuration file.

    This function opens the configuration file for writing (or creates it if it
    doesn't exist) and writes the specified Ghidra path to it.

    Args:
        path (str): The file path to the Ghidra installation to be saved to the
        configuration file.
    """
    with open("./conf/main.conf", mode='w', encoding='utf-8') as f:
        f.write(path)


def main():
    """
    Main function to manage the Ghidra path configuration.

    This function first attempts to retrieve the Ghidra path from the
    configuration file. If not found, it tries to find the Ghidra installation
    automatically from standard locations. If still not found, it prompts the
    user to input the Ghidra path, which is then saved to the configuration
    file for future use.
    """
    ghidra_path = get_ghidra_path_from_config()

    if not ghidra_path:
        ghidra_path = find_ghidra_installation()

    if not ghidra_path:
        ghidra_path = input("Please enter the path to your Ghidra installation: ")
        save_ghidra_path_to_config(ghidra_path)

    print(f"Using Ghidra installation at: {ghidra_path}")

if __name__ == "__main__":
    main()
