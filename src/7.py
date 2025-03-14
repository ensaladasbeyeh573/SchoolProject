import os

def get_projects():
    """Return a list of all projects in the current directory."""
    projects = []
    for file in os.listdir("."):
        if os.path.isdir(file) and not file.startswith("_"):
            projects.append(file)
    return projects