class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project_name, description, deadline=None):
        new_project = {
            "name": project_name,
            "description": description,
            "deadline": deadline if deadline is not None else 50
        }
        self.projects.append(new_project)

    def delete_project(self, project_name):
        for i, project in enumerate(self.projects):
            if project["name"] == project_name:
                del self.projects[i]
                break

    def view_projects(self):
        for project in self.projects:
            print(f"Project: {project['name']}, Description: {project['description']}, Deadline: {project['deadline']}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    projects = [
        {"name": "Python Basics", "description": "This is a Python basics course.", "deadline": None},
        {"name": "Data Structures and Algorithms", "description": "Learn about data structures and algorithms.", "deadline": 10}
    ]
    
    for project in projects:
        manager.add_project(project["name"], project["description"])
        print(f"Added project: {project['name']}")

    manager.view_projects()
