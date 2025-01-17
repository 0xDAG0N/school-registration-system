import sqlite3

class DataBaseHandler:
    """
    Handles interactions with the SQLite database for student data.
    """
    DB_NAME = 'students.db'  

    @staticmethod
    def _connect():
        """
        Establishes a connection to the SQLite database.
        """
        return sqlite3.connect(DataBaseHandler.DB_NAME)

    @staticmethod
    def create_table():
        """
        Creates the 'students' table in the database if it doesn't already exist.
        """
        with DataBaseHandler._connect() as conn: 
            conn.execute(
                '''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL)'''
            )

    @staticmethod
    def insert_student(name, email, age, gender):
        """
        Inserts a new student record into the 'students' table.
        """
        with DataBaseHandler._connect() as conn:
            conn.execute('INSERT INTO students (name, email, age, gender) VALUES (?, ?, ?, ?)',
                         (name, email, age, gender))

    @staticmethod
    def get_all_students():
        """
        Retrieves all student records from the 'students' table.

        Returns:
            list: A list of tuples, where each tuple represents a student record.
        """
        with DataBaseHandler._connect() as conn:
            # fetchall() retrieves all rows from the query result
            return conn.execute('SELECT * FROM students').fetchall()

# Create the table if it doesn't exist when the module is imported
DataBaseHandler.create_table()