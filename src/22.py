import os
os.system("clear")
print("Welcome to SchoolProject!")
user_input = input("Enter your project name: ")
project_path = f"C:/Users/{user_input}/Documents/MyProjects"
if not os.path.exists(project_path):
    print(f"Project '{user_input}' does not exist.")
else:
    print(f"Project '{user_input}' exists. Moving to the next directory...")
