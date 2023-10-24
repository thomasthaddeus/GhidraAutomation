#!/bin/bash

# Change to the directory where the script is located
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "./venv/bin/activate" ]; then
    source ./venv/bin/activate
fi

# Run pytest to execute all tests
pytest tests/

# Deactivate virtual environment if it was activated
if [ -d "./venv/bin/activate" ]; then
    deactivate
fi
