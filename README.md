# Code Decompiler CLI

This tool provides a command-line interface (CLI) to automatically decompile binaries using Ghidra.

## Prerequisites

- Ghidra (Version 10.3.2 or newer recommended)
- Python 3.x

## Installation

1. Ensure Ghidra is installed on your system.
2. Update the `GHIDRA_PATH` variable in the `decompile_cli.py` script to point to your Ghidra installation directory.
3. Clone this repository or download the necessary scripts (`decompile_cli.py` and `ExportDecompiledCode.java`).
4. Optionally, run the `install_tools.sh` script to copy the necessary files to the correct location (if provided):

   ```bash
   chmod +x install_tools.sh
   ./install_tools.sh
   ```

## Usage

Once installed, you can use the `decompile_cli.py` script to decompile binaries:

```bash
python3 /usr/local/bin/decompile_tools/decompile_cli.py -b <path_to_binary> -o <output_directory>
```

**Arguments:**

- `-b` or `--binary`: The path to the binary you want to decompile.
- `-o` or `--output`: The directory where you want to save the decompiled code.

## Features

- Automated decompilation without having to manually open Ghidra.
- Outputs Ghidra's stdout and stderr for debugging purposes.
- Saves decompiled code to the specified directory.

## Limitations

- Currently, the tool supports ELF binaries for 64-bit Linux systems. Support for other binary formats and platforms may be added in future versions.
- The tool assumes Ghidra's `analyzeHeadless` script is accessible through the specified `GHIDRA_PATH`.
- The `ExportDecompiledCode.java` script should be located at `../java/ExportDecompiledCode.java` relative to the `decompile_cli.py` script, or its path should be updated in the script.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss proposed changes or report bugs.

## License

This tool is released under the MIT License. See `LICENSE` for more details.
