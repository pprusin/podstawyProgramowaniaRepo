import os
import unittest

def file_exists_in_directory(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

class TestFileExistence(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_directory'
        self.existing_file = 'test_file.txt'
        self.non_existing_file = 'non_existent_file.txt'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, self.existing_file), 'w') as f:
            f.write("This is a test file.")

    def tearDown(self):
        os.remove(os.path.join(self.test_dir, self.existing_file))
        os.rmdir(self.test_dir)

    def test_existing_file(self):
        self.assertTrue(file_exists_in_directory(self.test_dir, self.existing_file))

    def test_non_existing_file(self):
        self.assertFalse(file_exists_in_directory(self.test_dir, self.non_existing_file))

    def test_file_in_non_existing_directory(self):
        self.assertFalse(file_exists_in_directory('non_existent_directory', self.existing_file))

if __name__ == '__main__':
    unittest.main()
