import sqlite3
from sqlite3 import Error

def commit():
    """
    Commits updates to spotify database
    
    Return:
    None
    """
    print "commit"
    conn.commit()


def create_database():
    """
    - Creates and connects to the spotify database
    - Returns the connection and cursor to spotify database
    """
    
    # connect to default database
    conn = sqlite3.connect("default.db")
    cur = conn.cursor()
    
    
    # create spotify database
    cur.execute("DROP DATABASE IF EXISTS spotify")
    cur.execute("CREATE DATABASE spotify")

    # close connection to default database
    conn.close()    
    
    # connect to spotify database
    conn = sqlite3.connect("spotify.db")
    cur = conn.cursor()
    commit()
    
    return cur, conn


def create_connection():
    """ Create a connection to the SQLite spotify database
    
    Returns:
    Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(spotify.db)
    except Error as e:
        print(e)

    return conn
  
  
  def create_tables(conn):
    """
    Create a new table
    Parameters:
    conn - connection to the sqlite database
    
    Returns:
    None
    """
    for query in create_table_queries:
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return cur.lastrowid
  
  
def main():
    """
    - Drops (if exists) and Creates the spotify database. 
    
    - Establishes connection with the spotify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print("The connection to the spotify database is now closed.")


if __name__ == "__main__":
    main()
