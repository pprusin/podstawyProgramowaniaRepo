import unittest
import sqlite3

def execute_query(db_name, query):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

class TestDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.db_name = ':memory:'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
        self.cursor.execute('INSERT INTO test (name) VALUES ("Alice")')
        self.cursor.execute('INSERT INTO test (name) VALUES ("Bob")')
        self.cursor.execute('INSERT INTO test (name) VALUES ("Charlie")')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_query_all_rows(self):
        query = 'SELECT * FROM test'
        expected_results = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
        results = execute_query(self.db_name, query)
        self.assertEqual(results, expected_results)

    def test_query_single_row(self):
        query = 'SELECT * FROM test WHERE name = "Bob"'
        expected_results = [(2, 'Bob')]
        results = execute_query(self.db_name, query)
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
