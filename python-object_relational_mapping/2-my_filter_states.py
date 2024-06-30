#!/usr/bin/python3
"""
    The `Filter states by user input` module
"""
import MySQLdb
import sqlalchemy
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""
                    SELECT * FROM states
                    WHERE name = "{:s}"
                    ORDER BY id ASC
                """.format(name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()
