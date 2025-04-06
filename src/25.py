import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/add_project', methods=['POST'])
def add_project():
    data = request.get_json()
    project_name = data['project_name']
    description = data['description']
    
    # Add new project to the database
    with open('projects.json', 'r') as file:
        projects = json.load(file)
    projects.append({'name': project_name, 'description': description})
    
    with open('projects.json', 'w') as file:
        json.dump(projects, file)
    
    return "Project added successfully"

if __name__ == '__main__':
    app.run(debug=True)
