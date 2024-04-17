import unittest
import json
from file_operations import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_file"
        self.expected_project_data = {"Project": self.file_name, "Tasks": []}
        self.project_data = {"Project": "TestProject", "Tasks": ["Task 1", "Task 2", "Task 3"]}

    def test_read_project_data_from_txt(self):
        project_data_txt = FileManager.read_project_data_from_txt(self.file_name)
        self.assertEqual(project_data_txt, self.expected_project_data)

    def test_save_project_data_to_json(self):
        FileManager.save_project_data_to_json(self.project_data, self.file_name)

        with open(f"{self.file_name}.json", "r") as file:
            saved_project_data = json.load(file)
        self.assertEqual(saved_project_data, self.project_data)

    def test_load_project_data_from_json(self):
        loaded_project_data = FileManager.load_project_data_from_json(self.file_name)
        self.assertEqual(loaded_project_data, self.project_data)


if __name__ == '__main__':
    unittest.main()

