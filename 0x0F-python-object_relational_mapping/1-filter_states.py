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

    conn = MySQLdb.connect(host=host, port=port, user=username,
                           passwd=password, db=db_name)
    cr = conn.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    record = cr.fetchall()

    for item in record:
        print(item)
    cr.close()
    conn.close()


if __name__ == "name":
    filter_all()
