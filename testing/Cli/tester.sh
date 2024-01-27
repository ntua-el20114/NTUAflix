#!/bin/bash

# Directory containing the .py files
DIRECTORY="./"
python3 login.py;

# Iterate over each .py file in the directory
for file in "$DIRECTORY"/*.py; do
    # Extract the filename from the path
    filename=$(basename "$file")

    # Skip specific files
    if [[ "$filename" == "login.py" || "$filename" == "logout.py" ]]; then
        echo "Skipping $filename"
        continue
    fi

    echo "Running test: $file"
    python "$file"
    echo "Test finished"
    echo
done

python3 logout.py;
