import subprocess

def extract_strings(binary_path):
    """
    Extract strings from the given binary using the `strings` command.
    Return the extracted strings as a list.
    """
    try:
        result = subprocess.run(['strings', binary_path], capture_output=True, check=True, text=True)
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Error running strings on {binary_path}: {e}")
        return []
