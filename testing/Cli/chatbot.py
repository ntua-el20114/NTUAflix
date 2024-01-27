import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = [
    "python",                  # the Python interpreter
    "../../cli-client/se2344.py",  # the path to your Python script
    "chatbot",                    # the command
    "--param1", "Hello",   # a prompt
]


# Run the command and capture the output and return code
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Command Output: \n", result.stdout)