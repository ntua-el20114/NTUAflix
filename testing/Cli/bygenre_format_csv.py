import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = [
    "python",                   # the Python interpreter
    "../../cli-client/se2344.py",  # the path to your Python script
    "bygenre",              # the command
    "--param1", "Action",          # additional command arguments
    "--param2", "0",
    "--param3", "1900",          # additional command arguments
    "--param4", "1990",
    "--format", "csv",
]

# Run the command and capture the output and return code
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Command Output:", result.stdout)
