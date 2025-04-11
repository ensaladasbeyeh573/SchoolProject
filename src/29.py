import os
from pathlib import Path

def main():
    # Define paths to your project and files
    project_path = Path("/path/to/your/project")
    
    # Ensure the path exists
    if not project_path.is_dir():
        print("Error: Project directory does not exist.")
        return
    
    # Iterate through all files in the project
    for file_name in project_path.iterdir():
        # Check if the file is a Python script
        if file_name.suffix == ".py":
            # Get the file's path
            file_path = str(file_name)
            
            # Change directory to the project root
            os.chdir(project_path)
            
            # Run the Python script with pyhton as the interpreter
            exec(open(file_path).read())
            
            # Reset the current working directory back to the original
            os.chdir("..")
