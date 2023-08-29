#!/usr/bin/python3
""" script that lists all cities """
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cursor = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
