"""logger.py

The log_utils module provides a utility function to manage log rotation in a specified directory.

The logrotate function within this module helps in managing log files by
renaming existing log files, creating a new log file for fresh logging, and
deleting old log files beyond a specified retention limit. This utility is
essential for maintaining a clean and manageable logging system, preventing the
log directory from being cluttered with an excessive number of log files.

Functions:
    logrotate(log_dir='logs', max_logs=5): Rotates log files in the specified directory.
"""

import os
import logging
import glob
import shutil


# Define constants for logging levels
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger with specified parameters."""
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

    # Create a file handler and set level to debug
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(formatter)

    # Create logger and set level
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger

def logrotate(log_dir='../logs/', max_logs=5):
    """
    Rotate log files in the specified directory.

    This function manages log files by performing the following operations:
    1. Renames existing log files by appending a numeric suffix, incrementing the suffix for each file.
    2. Creates a new log file named log_0.txt for fresh logging.
    3. Deletes old log files if the total number of log files exceeds the specified maximum limit.

    The renaming and deletion operations help in maintaining a clean and manageable logging system, ensuring that the log directory doesn't get cluttered with an excessive number of log files.

    Args:
        log_dir (str, optional): The directory containing the log files. Defaults to 'logs'.
        max_logs (int, optional): The maximum number of log files to retain. Defaults to 5.

    Returns:
        str: The path of the new log file created for fresh logging.
    """
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Get a list of existing log files
    log_files = sorted(glob.glob(os.path.join(log_dir, 'log_*.txt')))

    # Rename existing log files
    for i, log_file in enumerate(reversed(log_files), start=1):
        new_name = os.path.join(log_dir, f'log_{i}.txt')
        shutil.move(log_file, new_name)

    # Create a new log file for fresh logging
    new_log_file = os.path.join(log_dir, 'log_0.txt')
    with open(new_log_file, mode='w', encoding='utf-8') as f:
        pass  # New log file created

    # Delete old log files if the number of log files exceeds max_logs
    log_files = sorted(glob.glob(os.path.join(log_dir, 'log_*.txt')))
    for log_file in log_files[max_logs:]:
        os.remove(log_file)

    # Return the path of the new log file for further use
    return new_log_file


# Default logger for the application
app_logger = setup_logger("app", "app.log")

# Logger for test results
test_logger = setup_logger("tests", "tests.log")
