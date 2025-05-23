import os

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist.")
    
    with open(filename, "r") as file:
        return file.read()

# Example usage
write_file("project.log", "This is the content to be written in 'project.log' file.\n")
print(read_file("project.log"))
