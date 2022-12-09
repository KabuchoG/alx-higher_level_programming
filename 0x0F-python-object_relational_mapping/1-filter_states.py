#!/usr/bin/python3
"""Filter Select using MySQLdb"""

import sys
import MySQLdb


def filter_all():
    """ filter names with N"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host, user=username,
                           passwd=password, db=db_name, port=port)
    cr = conn.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    record = cr.fetchall()

    n_list = []
    for item in record:
        n_list.append(item)
    if n_list is not None:
        for state in n_list:
            print(state)
    cr.close()
    conn.close()


if __name__ == "name":
    filter_all()
