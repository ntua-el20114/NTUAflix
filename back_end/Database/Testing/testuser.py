import unittest
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'database': 'ntuaflix',
}

class TestAppUserDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    def test_delete_user(self):
        insert_query = '''
            INSERT INTO app_user (user_role, token, first_name, last_name, birthdate, email, username, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        delete_query = 'DELETE FROM app_user WHERE id = %s'

        self.cursor.execute(insert_query, ('standard_user', 'token123', 'John', 'Doe', '1980-01-01', 'john@example.com', 'johndoe', 'password123'))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM app_user WHERE username = %s', ('johndoe',))
        row_before_deletion = self.cursor.fetchone()
        self.assertIsNotNone(row_before_deletion, "Insertion failed, 'John Doe' user doesn't exist")

        self.cursor.execute(delete_query, (row_before_deletion[0],))  # Assuming id is auto-incremented primary key
        self.conn.commit()

        self.cursor.execute('SELECT * FROM app_user WHERE username = %s', ('johndoe',))
        row_after_deletion = self.cursor.fetchone()
        self.assertIsNone(row_after_deletion, "Deletion failed, 'John Doe' user still exists")

    def test_insert_and_query_user(self):
        insert_query = '''
            INSERT INTO app_user (user_role, token, first_name, last_name, birthdate, email, username, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        data = ('administrator', 'token456', 'Jane', 'Smith', '1975-05-15', 'jane@example.com', 'janesmith', 'pass123')

        self.cursor.execute(insert_query, data)
        self.conn.commit()

        self.cursor.execute('SELECT * FROM app_user WHERE username = %s', ('janesmith',))
        row = self.cursor.fetchone()
        self.assertIsNotNone(row, "Insertion failed for 'Jane Smith' user, data doesn't exist")

    def test_delete_non_existent_user(self):
        delete_query = 'DELETE FROM app_user WHERE id = %s'

        non_existent_id = '1000'
        self.cursor.execute(delete_query, (non_existent_id,))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM app_user WHERE id = %s', (non_existent_id,))
        row = self.cursor.fetchone()
        self.assertIsNone(row, "Deletion failed for non-existent user, entry still exists")

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()

