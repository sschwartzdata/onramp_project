import sqlite3
from sqlite3 import Error

# Commit changes to database
def commit():
    """
    Commits updates to spotify database
    
    Return:
    None
    """
    print ("commit")
    conn.commit()


# Creates connection to database and cursor
def create_connection(db_path):
    """
    - Creates and connects to the spotify database
    - Returns the connection and cursor to spotify database
    """

    # connect to spotify database
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        print("Successfully connected to the database")
    except Exception as e:
        print("Error during connection: ", str(e))
    
    return cur, conn

# Executes DROP TABLE SQL queries  
def drop_tables(conn):
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
 
 # Executes CREATE TABLE SQL queries   
def create_tables(conn):
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
  
  
def main():
    """
    - Drops (if exists) and Creates the spotify database. 
    
    - Establishes connection with the spotify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    database = r"C:\Users\sbsch\Desktop\spotify.db"
    cur, conn = create_connection(database)
    drop_tables(conn)
    create_tables(conn)


    conn.close()
    print("The connection to the spotify database is now closed.")


if __name__ == "__main__":
    main()
