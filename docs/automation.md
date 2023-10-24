# Documentation

## Automation

### 1. Ghidra Script

First, you'll need to create and save the Ghidra script `ExportDecompiledCode.java` (as provided in the previous answer) in Ghidra's script directory.

### 2. Python CLI Tool

Here's a basic Python script to automate the process:

```python
import subprocess
import os
import argparse

GHIDRA_PATH = "/path/to/ghidra_10.4_PUBLIC"  # Modify this to your Ghidra installation path
GHIDRA_SCRIPT_PATH = "/path/to/ExportDecompiledCode.java"  # Modify this to the path where you saved the Ghidra script

def decompile_binary(binary_path, output_path):
    # Construct the command for Ghidra's headless analyzer
    cmd = [
        os.path.join(GHIDRA_PATH, "support", "analyzeHeadless"),
        ".",  # Project directory (you can customize this)
        "TempProject",  # Temporary project name (you can customize this)
        "-import", binary_path,
        "-postScript", GHIDRA_SCRIPT_PATH,
        output_path,  # This will be passed as an argument to the Ghidra script
        "-deleteProject"  # Delete the temporary project after analysis
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
```

### 3. Usage

You can then run the script from the command line:

```bash
python your_script_name.py /path/to/binary /path/to/output.txt
```

Make sure to update the paths (`GHIDRA_PATH` and `GHIDRA_SCRIPT_PATH`) in the Python script to point to your Ghidra installation and Ghidra script, respectively.

This Python script will run Ghidra's headless analyzer, import the provided binary, run the Ghidra script to decompile the binary, and then save the output to the specified file, all without opening the Ghidra GUI.
