#!/usr/bin/python3
"""Credentials"""

import sys
import MySQLdb
username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
search_name = sys.argv[4]
host = 'localhost'
port = 3306

connection = MySQLdb.connect(host=host, user=username,
                       passwd=password, db=db_name, port=port)
cursor = connection.cursor()