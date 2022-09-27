def db_comp(df_list, queries, con):
    """
    Obtains the number of records in each table in the database and compares
    that to the number of records in the original dataframe

    Parameters:
    df_list: Lits of (dataframe, name) tuples
    queries: List of queries that return the number of records in each table
    con: connection to the database

    Returns:
    None
    """
    row_values = []
    for query in queries:
        try:
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchone()
            row_values.append(int(rows))
        except Exception as e:
            print(e)

    for i in range(0, 4):
        print("Records not converted to" + df_list[i][1] + "realation:")
        print(str(df_list[i][0]) - row_values[i])
