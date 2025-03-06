class ProjectManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.projects = []
        
    def add_project(self, project_name):
        self.projects.append(project_name)
    
    def get_all_projects(self):
        return self.projects
    
    def remove_project(self, project_name):
        if project_name in self.projects:
            self.projects.remove(project_name)
