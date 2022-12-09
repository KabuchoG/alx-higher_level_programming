#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

def print_search():
    """prints a state by search name"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    connection = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = \"{}\" ORDER BY id ASC;").format(search_name)
    query = cursor.fetchall()

    for row in query:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    print_search()
    