#!/usr/bin/python3
"""
    The `SQL Injection...` module
"""
import MySQLdb
import sqlalchemy
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]
    name = str(name.split(chr(39))[0])
    name = str(name.split(chr(34))[0])

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""
                    SELECT * FROM states
                    WHERE name = "{}"
                    ORDER BY id ASC
                """.format(name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == name:
            print(row)
    cur.close()
    conn.close()
