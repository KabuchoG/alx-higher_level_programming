#!/usr/bin/python3
"""MySQLdb"""

import sys
import MySQLdb


def list_all():
    """ List all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, user=username, passwd=password,
                           db=db_name, port=port)
    curs = conn.cursor()
    curs.execute('SELECT cities.id, cities.name,\
        states.name FROM cities INNER JOIN states\
        ON cities.states_id = states.id ORDER BY cities.id ASC;')
    records = curs.fetchall()
    for name in records:
        print(name)

    curs.close()
    conn.close()


if __name__ == "__main__":
    list_all()
