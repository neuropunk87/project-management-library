class ProjectNotFoundError(Exception):
    def __init__(self, message="Project not found. Please check the project name."):
        self.message = message
        super().__init__(self.message)


class TaskNotFoundError(Exception):
    def __init__(self, message="Task not found in the project. Please check the task name."):
        self.message = message
        super().__init__(self.message)

