#!/usr/bin/python3
"""MySQLdb"""

import sys
import MySQLdb


def list_all():
    """ List all states"""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, user=user, pwd=password, db=db_name, port=port)

    curs = conn.cursor()

    curs.execute('SELECT * FROM States')

    records = curs.fetchall()

    for name in records:
        print(name)

if __name__ == "main":
    list_all()