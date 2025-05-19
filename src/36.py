import os
import hashlib

def create_project_directory(directory_name):
    # Generate file name hash using SHA256 algorithm
    file_hash = hashlib.sha256(os.path.join(directory_name, "project.txt")).hexdigest()
    
    # Create a temporary directory for project files
    temp_dir = os.path.join("temp", "projects")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Move project files into the temp directory with updated file name hash
    for root, dirs, files in os.walk(os.path.join(directory_name, "project"), topdown=False):
        for filename in files:
            old_file = os.path.join(root, filename)
            new_file = os.path.join(temp_dir, f"{file_hash}_{filename}")
            os.rename(old_file, new_file)

if __name__ == "__main__":
    directory_name = "/path/to/your/directory"  # replace with your project's directory path
    create_project_directory(directory_name)
