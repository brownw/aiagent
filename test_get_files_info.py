from functions.get_files_info import get_files_info
import unittest


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self) -> None:
        self.get_files_info = get_files_info

    def test_get_files_info(self) -> None:
        result = self.get_files_info("calculator", ".")
        print(result)
        self.assertEqual(result, 'Success: "." is within the working_directory')

    def test_get_files_info_absolute_path(self) -> None:
        result = self.get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(
            result,
            'Error: Cannot list "/bin" as it is outside the permitted working_directory',
        )

    def test_get_files_info_parent_directory(self) -> None:
        result = self.get_files_info("calculator", "../")
        print(result)
        self.assertEqual(
            result,
            'Error: Cannot list "../" as it is outside the permitted working_directory',
        )

    def test_get_files_info_file(self) -> None:
        result = self.get_files_info("calculator", "main.py")
        print(result)
        self.assertEqual(result, 'Error: "main.py" is not a directory')

if __name__ == "__main__":
    unittest.main()