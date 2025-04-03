def calculate_total_cost(project_data):
    total_cost = 0
    for project in project_data:
        cost_per_project = float(project['cost'])
        total_cost += cost_per_project
    return total_cost

project_data = [
    {"name": "Project A", "cost": 100.5},
    {"name": "Project B", "cost": 89.7}
]
total_cost = calculate_total_cost(project_data)
print(f"The total cost for all projects is: {total_cost}")
