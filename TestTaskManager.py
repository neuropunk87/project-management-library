import unittest
from tasks import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.project_name = "TestProject"
        self.task_name = "TestTask"
        self.new_task_name = "TestNewTask"
        self.responsible = "John Doe"
        self.new_responsible = "Jane Doe"
        self.status = "Assigned"
        self.new_status = "Completed"
        self.deadline = "2023-04-13 12:00:00"
        self.new_deadline = "2023-04-15 12:00:00"

    def test_add_task(self):
        TaskManager.add_task(self.project_name, self.task_name, self.responsible, self.status, self.deadline)

    def test_view_task(self):
        tasks = TaskManager.view_tasks(self.project_name)
        self.assertIsInstance(tasks, list)

    def test_update_task(self):
        TaskManager.update_task(self.project_name, self.task_name, self.new_task_name, self.new_responsible,
                                self.new_status, self.new_deadline)
        tasks = TaskManager.view_tasks(self.project_name)
        expected_task = (f"{self.new_task_name} -> Responsible: {self.new_responsible}, Status: {self.new_status}, "
                         f"Deadline: {self.new_deadline}\n")
        self.assertIn(expected_task, tasks)

    def test_remove_task(self):
        TaskManager.remove_task(self.project_name, self.new_task_name)
        removed_tasks = TaskManager.view_tasks(self.project_name)
        self.assertNotIn(f"{self.new_task_name} -> Responsible: {self.new_responsible}, Status: {self.new_status}, "
                         f"Deadline: {self.new_deadline}", removed_tasks)


if __name__ == '__main__':
    unittest.main()

