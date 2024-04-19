from exceptions import ProjectNotFoundError, TaskNotFoundError


class TaskManager:
    @staticmethod
    def add_task(project_name, task_name, responsible, status, deadline):
        try:
            if project_name and task_name:
                with open(f"{project_name}.txt", "r") as file:
                    file.readlines()
                with open(f"{project_name}.txt", "a") as file:
                    file.write(f"{task_name} -> Responsible: {responsible}, Status: {status}, Deadline: {deadline}\n")
                    print(f"---> Task '{task_name}' added to project '{project_name}'!")
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{project_name}' not found.")

    @staticmethod
    def view_tasks(project_name):
        try:
            with open(f"{project_name}.txt", "r") as file:
                tasks = file.readlines()
                print(*tasks)
                return tasks
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{project_name}' not found.")

    @staticmethod
    def update_task(project_name, task_name, new_task_name, new_responsible, new_status, new_deadline):
        try:
            with open(f"{project_name}.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{project_name}' not found.")
            return

        updated_lines = []
        task_found = False
        for line in lines:
            if task_name in line:
                task_found = True
                updated_lines.append(f"{new_task_name} -> Responsible: {new_responsible}, Status: {new_status}, "
                                     f"Deadline: {new_deadline}\n")
                with open(f"{project_name}.txt", "w") as file:
                    file.writelines(updated_lines)
                    print(f"---> Task '{new_task_name}' updated in project '{project_name}'!")
                    print(f"{new_task_name} -> Responsible: {new_responsible}, Status: {new_status}, "
                          f"Deadline: {new_deadline}\n")
            else:
                updated_lines.append(line)

        if not task_found:
            print(f"---> {TaskNotFoundError()}")
            # print(f"---> Task '{task_name}' not found in project '{project_name}'.")
            return

    @staticmethod
    def remove_task(project_name, task_name):
        try:
            task_found = False
            with open(f"{project_name}.txt", "r") as file:
                lines = file.readlines()
            with open(f"{project_name}.txt", "w") as file:
                for line in lines:
                    if not line.startswith(f"{task_name}"):
                        file.write(line)
                    else:
                        task_found = True
                        print(f"---> Task '{task_name}' removed from project '{project_name}'!")
            if not task_found:
                print(f"---> {TaskNotFoundError()}")
                # print(f"---> Task '{task_name}' not found in project '{project_name}'.")
        except FileNotFoundError:
            print(f"---> {ProjectNotFoundError()}")
            # print(f"---> Project '{project_name}' not found.")

