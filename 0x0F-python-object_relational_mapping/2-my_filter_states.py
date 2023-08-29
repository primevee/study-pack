#!/usr/bin/python3
"""module takes an argument and"""
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search_word = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cursor = db.cursor()

    query = ("SELECT * FROM states "
             "WHERE BINARY name = '{}' "
             " ORDER BY id ASC").format(search_word)
    query = query.format(search_word)
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
