import sqlite3
from sqlite3 import Error



def create_views(con, queries):
    """
    - Creates and connects to the spotify database
    - Returns the connection and cursor to spotify database
    """
    i=0
    for query in queries:
        # connect to spotify database
        print(i)
        cur = con.cursor()
        cur.execute(query)
        i +=1
