"""main.py
This script provides utility functions for interacting with the Ghidra software
suite and managing configurations for analysis tasks.

The main functionalities include finding the Ghidra installation directory,
getting and saving configurations, and offering an interactive interface for
the user to specify Ghidra path and output directory, as well as to choose
whether to extract strings from a specified binary file.

The script utilizes a couple of external modules: `utils.string_util` for
string extraction and `config_manager` for handling configuration.

Returns:
    None: This script is intended to be run as a standalone utility, and does
    not return any values when executed.
"""

import os
from utils.string_util import extract_strings
from config_manager import get_config, save_config

GHIDRA_SCRIPT = "support/analyzeHeadless"
CONFIG_FILE = "../conf/main.conf"

# List of standard locations to check for Ghidra installation
STANDARD_LOCATIONS = ["/usr/bin/ghidra", "/usr/local/bin/ghidra", "/opt/ghidra"]


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

def main():
    """
    Main function to interactively manage Ghidra configurations and optionally
    extract strings.

    This function starts by fetching existing configurations for Ghidra path
    and output directory. If these configurations are not set, it attempts to
    automatically find the Ghidra installation, or prompts the user to specify
    it. It also allows the user to specify an output directory, and decide
    whether to extract strings from a binary file. If the user chooses to
    extract strings, it prompts for the binary file path, extracts strings from
    it, and saves them to a file in the output directory.
    """
    ghidra_path, output_dir = get_config()

    if not ghidra_path:
        ghidra_path = find_ghidra_installation()

    if not ghidra_path:
        ghidra_path = input("Please enter the path to your Ghidra installation: ")

    if not output_dir:
        output_dir = os.getcwd()

    # Optionally allow user to specify an output directory
    custom_output = input(
        f"Press Enter to use the default output directory [{output_dir}] or provide a new one: "
    )
    if custom_output:
        output_dir = custom_output

    save_config(ghidra_path, output_dir)

    print(f"Using Ghidra installation at: {ghidra_path}")
    print(f"Using output directory: {output_dir}")

    # Check if the user wants to extract strings from the binary
    extract_strings_choice = input(
        "Do you want to extract strings from the binary? (yes/no): "
    ).lower()
    if extract_strings_choice == "yes":
        binary_path = input("Please enter the path to the binary: ")
        if os.path.exists(binary_path):
            strings_data = extract_strings(binary_path)
            # Save the extracted strings to a file in the output directory
            with open(
                os.path.join(output_dir, "strings_output.txt"),
                mode="w",
                encoding="utf-8",
            ) as f:
                f.write("\n".join(strings_data))
            print(
                f"Extracted strings saved to: {os.path.join(output_dir, 'strings_output.txt')}"
            )
        else:
            print(f"Binary not found at {binary_path}")

if __name__ == "__main__":
    main()
