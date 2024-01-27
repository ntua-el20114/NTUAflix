import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = [
    "python",                  # the Python interpreter
    "../../cli-client/se2344.py",  # the path to your Python script
    "name",                    # the command
    "--param1", "nm0000019",   # additional command arguments
    "--format", "csv"
]


# Run the command and capture the output and return code
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Command Output: \n", result.stdout)


