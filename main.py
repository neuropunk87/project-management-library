from projects import ProjectManager
from tasks import TaskManager
from file_operations import FileManager
from datetime import datetime


print("---> Project Management Library <---")
print("---> Menu:")


def main_menu():
    project_manager = ProjectManager()
    task_manager = TaskManager()
    file_manager = FileManager()

    while True:
        print("\n1. Create Project")
        print("2. Update Project")
        print("3. Delete Project")
        print("4. View List of Projects")
        print("5. Add Task to Project")
        print("6. View Project Tasks")
        print("7. Update Task in Project")
        print("8. Remove Task from Project")
        print("9. Save Project Data to JSON")
        print("10. Output Project Data in JSON")
        print("11. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            project_name = input("Enter project name: ")
            project_manager.create_project(project_name)
        elif choice == "2":
            current_name = input("Enter current project name: ")
            new_name = input("Enter new project name: ")
            project_manager.update_project(current_name, new_name)
        elif choice == "3":
            project_name = input("Enter project name: ")
            project_manager.delete_project(project_name)
        elif choice == "4":
            project_manager.view_projects()
        elif choice == "5":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            responsible = input("Enter responsible person: ")
            status = "Assigned"
            deadline = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_manager.add_task(project_name, task_name, responsible, status, deadline)
        elif choice == "6":
            project_name = input("Enter project name: ")
            task_manager.view_tasks(project_name)
        elif choice == "7":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            new_task_name = input("Enter new task name: ")
            new_responsible = input("Enter new responsible person: ")
            new_status = input("Enter new task status: ")
            new_deadline = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_manager.update_task(project_name, task_name, new_task_name, new_responsible, new_status, new_deadline)
        elif choice == "8":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            task_manager.remove_task(project_name, task_name)
        elif choice == "9":
            txt_file_name = input("Enter project filename in '.txt' format: ")
            json_file_name = input("Enter filename for saving in '.json' format: ")
            project_data = file_manager.read_project_data_from_txt(txt_file_name)
            file_manager.save_project_data_to_json(project_data, json_file_name)
        elif choice == "10":
            json_file_name = input("Enter filename in '.json' format for output: ")
            file_manager.load_project_data_from_json(json_file_name)
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()

