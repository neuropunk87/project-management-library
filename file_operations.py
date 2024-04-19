import json
from exceptions import ProjectNotFoundError


class FileManager:
    @staticmethod
    def read_project_data_from_txt(file_name):
        try:
            with open(f"{file_name}.txt", "r") as file:
                project_data = {"Project": file_name, "Tasks": [line.strip() for line in file.readlines()]}
                return project_data
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{name}' not found.")

    @staticmethod
    def save_project_data_to_json(project_data, file_name):
        with open(f"{file_name}.json", "w") as file:
            json.dump(project_data, file)

    @staticmethod
    def load_project_data_from_json(file_name):
        try:
            with open(f"{file_name}.json", "r") as file:
                data = json.load(file)
                print(data)
                return data
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{name}' not found.")

