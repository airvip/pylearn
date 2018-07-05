#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

try:
    cursor =conn.cursor()
    # cursor.execute("DROP TABLE user")

    cursor.execute("select name from sqlite_master where type='table'")
    print(cursor.fetchall())

    sql = "CREATE TABLE IF NOT EXISTS user (" \
          "id INT(10) NOT NULL PRIMARY KEY, " \
          "name VARCHAR(20) NOT NULL DEFAULT '')"
    cursor.execute(sql)

    cursor.execute("select name from sqlite_master where type='table'")
    print(cursor.fetchall())
finally:
    conn.close()


