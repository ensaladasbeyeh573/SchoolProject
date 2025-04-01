import os

class ProjectManager:
    def __init__(self):
        self.projects = {}
    
    def add_project(self, project_name):
        if project_name not in self.projects:
            self.projects[project_name] = []
    
    def remove_project(self, project_name):
        if project_name in self.projects:
            del self.projects[project_name]
    
    def create_project(self, project_name, tasks):
        if project_name not in self.projects:
            self.add_project(project_name)
            for task in tasks:
                self.tasks.append(task)

    def complete_project(self, project_name, tasks):
        if project_name in self.projects and len(tasks) > 0:
            self.tasks = tasks
