def get_projects(user):
  projects = user.project_set.all()
  return projects
