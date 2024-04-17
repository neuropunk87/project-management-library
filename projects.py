import os
from exceptions import ProjectNotFoundError


class ProjectManager:
    @staticmethod
    def create_project(name):
        with open(f"{name}.txt", "w") as file:
            file.write("Project Info\n\nTasks:\n")
            print(f"---> Project '{name}' created successfully!")

    @staticmethod
    def update_project(name, new_name):
        try:
            if name:
                os.rename(f"{name}.txt", f"{new_name}.txt")
                print(f"---> Project '{name}' renamed to '{new_name}'!")
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{name}' not found.")

    @staticmethod
    def delete_project(name):
        try:
            if name:
                os.remove(f"{name}.txt")
                print(f"---> Project '{name}' deleted successfully!")
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{name}' not found.")

    @staticmethod
    def view_projects():
        projects = [file.split(".")[0] for file in os.listdir() if file.endswith(".txt")]
        if projects:
            print("---> List of Projects:")
            for project in projects:
                print(project)
        else:
            print("---> No projects found.")
        return projects

