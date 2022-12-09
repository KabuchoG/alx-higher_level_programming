#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""

from credentials import *

def print_search():
    """prints a state by search name"""

    sql = "SELECT * FROM states WHERE name=search_name"
    cursor.execute(sql)
    query = cursor.fetchall()

    for row in query:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    print_search()
    