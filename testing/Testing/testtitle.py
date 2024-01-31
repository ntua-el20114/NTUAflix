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
            INSERT INTO title (title_id, titleType, originalTitle, isAdult, startYear, runtimeMinutes, genres, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        delete_query = 'DELETE FROM title WHERE title_id = %s'

        self.cursor.execute(insert_query, ('1', 'movie', 'The Matrix', '0', 1999, 136, 'Action,Sci-Fi', 'https://example.com/matrix'))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM title WHERE title_id = %s', ('1',))
        row_before_deletion = self.cursor.fetchone()
        self.assertIsNotNone(row_before_deletion, "Insertion failed, 'The Matrix' data doesn't exist")

        self.cursor.execute(delete_query, ('1',))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM title WHERE title_id = %s', ('1',))
        row_after_deletion = self.cursor.fetchone()
        self.assertIsNone(row_after_deletion, "Deletion failed, 'The Matrix' data still exists")

    def test_insert_and_query_multiple_entries(self):
        insert_query = '''
            INSERT INTO title (title_id, titleType, originalTitle, isAdult, startYear, runtimeMinutes, genres, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        data = [
            ('1', 'movie', 'The Matrix', '0', 1999, 136, 'Action,Sci-Fi', 'https://example.com/matrix'),
            ('2', 'tvSeries', 'Breaking Bad', '0', 2008, 49, 'Crime,Drama,Thriller', 'https://example.com/breakingbad'),
        ]

        for entry in data:
            self.cursor.execute(insert_query, entry)
        self.conn.commit()

        for entry in data:
            self.cursor.execute('SELECT * FROM title WHERE title_id = %s', (entry[0],))
            row = self.cursor.fetchone()
            self.assertIsNotNone(row, f"Insertion failed for entry {entry[0]}, data doesn't exist")

    def test_delete_non_existent_data(self):
        delete_query = 'DELETE FROM title WHERE title_id = %s'

        non_existent_id = '1000'
        self.cursor.execute(delete_query, (non_existent_id,))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM title WHERE title_id = %s', (non_existent_id,))
        row = self.cursor.fetchone()
        self.assertIsNone(row, "Deletion failed for non-existent data, entry still exists")

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()

