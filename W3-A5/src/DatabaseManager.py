# ---------------------------------------------------------------
# DatabaseManager.py
# Author: Roxanne Prajapati
# Description:
#      DatabaseManager class manages DB connection and executes SQL queries.
# ---------------------------------------------------------------
import sqlite3

class DatabaseManager:
    def __init__(self, db_name="clinic.db"):
        try:
            # Create or connect to database file
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            raise ValueError(f"Database connection error: {error}")

    def execute(self, sql_query, params=None):
        # Generic query executor for insert/update/delete
        try:
            if params is None:
                self.cursor.execute(sql_query)
            else:
                self.cursor.execute(sql_query, params)

            self.connection.commit()

        except sqlite3.Error as error:
            raise ValueError(f"Database execution error: {error}")

    def fetch_all(self, sql_query, params=None):
        # Fetch result from select queries
        try:
            if params is None:
                self.cursor.execute(sql_query)
            else:
                self.cursor.execute(sql_query, params)

            return self.cursor.fetchall()

        except sqlite3.Error as error:
            raise ValueError(f"Database fetch error: {error}")

    def close(self):
        # Close the database connection
        try:
            if self.connection:
                self.connection.close()
        except sqlite3.Error as error:
            raise ValueError(f"Database close error: {error}")

