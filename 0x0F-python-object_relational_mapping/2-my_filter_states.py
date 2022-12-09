#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""

from credentials import *

def print_search():
    """prints a state by search name"""

    cursor.execute("SELECT * FROM states WHERE BINARY name = {} ORDER BY id ASC;").format(search_name)
    query = cursor.fetchall()

    for row in query:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    print_search()
    