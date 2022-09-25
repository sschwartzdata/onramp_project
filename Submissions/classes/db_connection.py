import sqlite3
from sqlite3 import Error
from helper_functions.sql_queries import *


class DatabaseGen:

    def __init__(self, db_path):
        self.db_path = db_path

    def create_connection(self):
        """
        - Creates and connects to the spotify database
        - Returns the connection and cursor to spotify database
        """

        # connect to spotify database
        try:
            conn = sqlite3.connect(self.db_path)
            print("Successfully connected to the database")
        except Exception as e:
            print("Error during connection: ", str(e))

        return conn

    def commit(self):
        """
        Commits changes to spotify database

        Return:
        None
        """
        print("commit")
        conn.commit()

    # Executes DROP TABLE SQL queries
    def drop_tables(self, conn, drop_table_queries):
        """
        Drops tables if the exist from the drop_tables_queries list
        If an error occurs, the error statement is printed

        Parameters:
        conn - connection to the sqlite database

        Returns:
        None
        """
        print("Dropping Tables if they exist.")
        for query in drop_table_queries:
            try:
                cur = conn.cursor()
                cur.execute(query)
                conn.commit()
            except Error as e:
                print(e)

    def create_tables(self, conn, create_table_queries):
        """
        Create a new tables from the create_tables_queries list
        If an error occurs, the error statement is printed

        Parameters:
        conn - connection to the sqlite database

        Returns:
        None
        """
        print("Creating tables.")
        for query in create_table_queries:
            try:
                cur = conn.cursor()
                cur.execute(query)
                conn.commit()
            except Error as e:
                print(e)
        print("Tables have been successfully created.")
