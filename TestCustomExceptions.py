import unittest
from exceptions import ProjectNotFoundError, TaskNotFoundError


class TestCustomExceptions(unittest.TestCase):
    def test_project_not_found_error(self):
        with self.assertRaises(ProjectNotFoundError) as context:
            raise ProjectNotFoundError()
        self.assertEqual(str(context.exception), "Project not found. Please check the project name.")

    def test_task_not_found_error(self):
        with self.assertRaises(TaskNotFoundError) as context:
            raise TaskNotFoundError()
        self.assertEqual(str(context.exception), "Task not found in the project. Please check the task name.")


if __name__ == '__main__':
    unittest.main()

