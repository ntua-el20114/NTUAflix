import unittest
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'database': 'ntuaflix',
}

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    def test_delete_data(self):
        insert_query = '''
            INSERT INTO name (name_id, primaryName, birthYear, deathYear, primaryProfession, url)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        delete_query = 'DELETE FROM name WHERE name_id = %s'

        self.cursor.execute(insert_query, ('1', 'John Doe', 1980, None, 'actor', 'https://example.com/johndoe'))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM name WHERE name_id = %s', ('1',))
        row_before_deletion = self.cursor.fetchone()
        self.assertIsNotNone(row_before_deletion, "Insertion failed, 'John Doe' data doesn't exist")

        self.cursor.execute(delete_query, ('1',))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM name WHERE name_id = %s', ('1',))
        row_after_deletion = self.cursor.fetchone()
        self.assertIsNone(row_after_deletion, "Deletion failed, 'John Doe' data still exists")

    def test_insert_and_query_multiple_entries(self):
        insert_query = '''
            INSERT INTO name (name_id, primaryName, birthYear, deathYear, primaryProfession, url)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        data = [
            ('1', 'John Doe', 1980, None, 'actor', 'https://example.com/johndoe'),
            ('2', 'Jane Smith', 1975, 2020, 'actress', 'https://example.com/janesmith'),
        ]

        for entry in data:
            self.cursor.execute(insert_query, entry)
        self.conn.commit()

        for entry in data:
            self.cursor.execute('SELECT * FROM name WHERE name_id = %s', (entry[0],))
            row = self.cursor.fetchone()
            self.assertIsNotNone(row, f"Insertion failed for entry {entry[0]}, data doesn't exist")

    def test_delete_non_existent_data(self):
        delete_query = 'DELETE FROM name WHERE name_id = %s'

        non_existent_id = '1000'
        self.cursor.execute(delete_query, (non_existent_id,))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM name WHERE name_id = %s', (non_existent_id,))
        row = self.cursor.fetchone()
        self.assertIsNone(row, "Deletion failed for non-existent data, entry still exists")

if __name__ == '__main__':
    unittest.main()

