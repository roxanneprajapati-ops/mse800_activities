# -----------------------------------------------------------------------------
# database_manager.py - SQLite database manager
# Author: Roxanne Prajapati
# Description:
#      SQLite connection, schema setup, and minimal persistence functions.
# -----------------------------------------------------------------------------
'''
database_manager.py
Singleton database manager for SQLite access.
'''

import sqlite3
from exchange_rate import ExchangeRate
from conversion import Conversion


class DatabaseError(Exception):
    '''
    Raised when a database operation fails.
    '''


class DatabaseManager:
    '''
    Singleton responsible for database connection, schema management,
    and persistence operations.
    '''

    _instance = None

    def __new__(cls):
        '''
        Ensure only one instance of DatabaseManager exists.

        :return: DatabaseManager instance.
        '''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def _connect(self):
        '''
        Create a SQLite connection if it does not already exist.

        :return: sqlite3.Connection instance.
        '''
        if self._connection is None:
            self._connection = sqlite3.connect('exchange.db')
            self._connection.row_factory = sqlite3.Row
        return self._connection

    def init_schema(self):
        '''
        Create database tables if they do not exist and seed a default rate.

        :return: None
        '''
        conn = self._connect()

        conn.execute(
            'CREATE TABLE IF NOT EXISTS exchange_rate ('
            'id INTEGER PRIMARY KEY, '
            'base_currency TEXT, '
            'target_currency TEXT, '
            'rate REAL, '
            'updated_at TEXT)'
        )

        conn.execute(
            'CREATE TABLE IF NOT EXISTS conversion ('
            'id INTEGER PRIMARY KEY, '
            'amount REAL, '
            'converted_amount REAL, '
            'rate_used REAL, '
            'timestamp TEXT)'
        )

        # Seed initial exchange rate if table is empty
        count = conn.execute('SELECT COUNT(*) FROM exchange_rate').fetchone()[0]
        if count == 0:
            conn.execute(
                'INSERT INTO exchange_rate VALUES (NULL, ?, ?, ?, ?)',
                ('NZD', 'USD', 0.60, ExchangeRate.now_iso())
            )

        conn.commit()

    def get_rate(self) -> ExchangeRate:
        '''
        Retrieve the most recent exchange rate.

        :return: ExchangeRate instance.
        '''
        conn = self._connect()
        row = conn.execute(
            'SELECT base_currency, target_currency, rate, updated_at '
            'FROM exchange_rate ORDER BY id DESC LIMIT 1'
        ).fetchone()

        if row is None:
            raise DatabaseError('No exchange rate found in database.')

        return ExchangeRate(*row)

    def insert_rate(self, rate: ExchangeRate):
        '''
        Save a new exchange rate record.

        :param rate: ExchangeRate instance.
        '''
        conn = self._connect()
        conn.execute(
            'INSERT INTO exchange_rate VALUES (NULL, ?, ?, ?, ?)',
            (rate.base_currency, rate.target_currency, rate.rate, rate.updated_at)
        )
        conn.commit()

    def insert_conversion(self, conversion: Conversion):
        '''
        Save a conversion record.

        :param conversion: Conversion instance.
        '''
        conn = self._connect()
        conn.execute(
            'INSERT INTO conversion VALUES (NULL, ?, ?, ?, ?)',
            (
                conversion.amount,
                conversion.converted_amount,
                conversion.rate_used,
                conversion.timestamp,
            )
        )
        conn.commit()
