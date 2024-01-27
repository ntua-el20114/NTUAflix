import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = [
    "python",                   # the Python interpreter
    "../../cli-client/se2344.py",  # the path to your Python script
    "searchtitle",              # the command
    "--param1", "Hen",          # additional command arguments
    #"--format", "csv"           # additional command arguments
]

# Run the command and capture the output and return code
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Command Output:", result.stdout)


