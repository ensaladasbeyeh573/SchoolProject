class ProjectManager:
    def __init__(self):
        self.projects = {}
    
    def add_project(self, name, description, deadline):
        project = {
            "name": name,
            "description": description,
            "deadline": deadline
        }
        self.projects[name] = project
    
    def list_projects(self):
        return list(self.projects.keys())
    
    def get_project(self, name):
        return self.projects[name]
    
    def remove_project(self, name):
        del self.projects[name]
    
    def update_deadline(self, name, new_deadline):
        self.get_project(name)["deadline"] = new_deadline

