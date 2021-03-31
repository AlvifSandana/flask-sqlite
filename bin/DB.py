import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def create_new_table(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)
