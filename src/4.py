import os

def create_project(name):
    project_path = os.path.join("Projects", name)
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    return project_path

if __name__ == "__main__":
    print(create_project("SchoolProject"))
