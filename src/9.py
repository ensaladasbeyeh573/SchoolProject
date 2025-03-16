import pandas as pd

def get_project(project_name):
    project = {
        "Name": project_name,
        "Description": f"This is a sample project for {project_name}.",
        "Status": "In Progress",
        "Deadline": "2023-04-15",
        "Assignees": ["John Doe", "Jane Smith"],
        "Priority": "High"
    }
    return project

def get_projects(project_names):
    projects = []
    for name in project_names:
        projects.append(get_project(name))
    return projects

def add_assignee(project_name, assignee):
    project = get_project(project_name)
    if assignee not in project["Assignees"]:
        project["Assignees"].append(assignee)
    return project

def remove_assignee(project_name, assignee):
    project = get_project(project_name)
    if assignee in project["Assignees"]:
        project["Assignees"].remove(assignee)
    return project

def change_priority(project_name, priority):
    project = get_project(project_name)
    project["Priority"] = priority
    return project

def update_status(project_name, status):
    project = get_project(project_name)
    project["Status"] = status
    return project

def update_deadline(project_name, deadline):
    project = get_project(project_name)
    project["Deadline"] = deadline
    return project

def delete_project(project_name):
    projects = get_projects()
    for i in range(len(projects)):
        if projects[i]["Name"] == project_name:
            del projects[i]
            break
    return projects