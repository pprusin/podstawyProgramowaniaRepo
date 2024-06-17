import unittest
import sqlite3

def connect_to_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

class TestDatabaseConnection(unittest.TestCase):
    def test_connection_successful(self):
        connection = connect_to_database(':memory:')  # Using an in-memory database
        self.assertIsNotNone(connection)
        connection.close()

    def test_connection_failure(self):
        connection = connect_to_database('non_existent_directory/non_existent.db')
        self.assertIsNone(connection)

if __name__ == '__main__':
    unittest.main()
