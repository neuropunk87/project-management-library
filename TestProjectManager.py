import unittest
import os
from projects import ProjectManager


class TestProjectManager(unittest.TestCase):
    # def setUp(self):
    #     with open("test_project.txt", "w") as file:
    #         file.write("Project Info\n\nTasks:\n")

    def test_create_project(self):
        ProjectManager.create_project("test_project")
        self.assertTrue(os.path.exists("test_project.txt"))
        ProjectManager.create_project("test_project1")
        ProjectManager.create_project("test_project2")

    def test_update_project(self):
        ProjectManager.update_project("test_project", "test_project_updated")
        self.assertTrue(os.path.exists("test_project_updated.txt"))
        self.assertFalse(os.path.exists("test_project.txt"))

    def test_delete_project(self):
        ProjectManager.delete_project("test_project_updated")
        self.assertFalse(os.path.exists("test_project_updated.txt"))

    def test_view_projects(self):
        projects = ProjectManager.view_projects()
        self.assertIn("test_project1", projects)
        # self.assertTrue("test_project1" in projects)


if __name__ == '__main__':
    unittest.main()

