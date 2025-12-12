# ---------------------------------------------------------------
# Database Manager
# Author: Roxanne Prajapati
# Description:
#      This class manages DB connection and executes SQL queries.
# ---------------------------------------------------------------

import sqlite3

class DatabaseManager:
    def __init__(self, db_name="college1.db"):
        # Create or connect to database file
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, sql_query, params=None):
        # Generic query executor for insert/update/delete
        if params is None:
            self.cursor.execute(sql_query)
        else:
            self.cursor.execute(sql_query, params)
        self.connection.commit()

    def fetch_all(self, sql_query, params=None):
        # Fetch result from select queries
        if params is None:
            self.cursor.execute(sql_query)
        else:
            self.cursor.execute(sql_query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
