#!/usr/bin/python3
"""script for getting states from sql db
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    usern = args[1]
    passw = args[2]
    data = args[3]
    db = MySQLdb.connect(host='loclahost', user=usern, passwd=passw, db=data, port=3306)
    cur = db.cursor()
    num_r = cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for r in rows:
        print(r)
