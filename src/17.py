import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return error, output

def main():
    # Replace this with your actual command or task
    if "your_command_here" in os.listdir("scripts"):
        command = "source scripts/your_command_here"
    else:
        print("No script found.")
    
    result_error, result_output = run_command(command)
    if result_error:
        print(f"An error occurred: {result_error}")
    elif result_output:
        print(f"Script output: {result_output}")

if __name__ == "__main__":
    main()
