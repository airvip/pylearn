#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

try:
    cursor =conn.cursor()

    cursor.execute("select * from user")
    print(cursor.fetchall())

    sql = "UPDATE `user` SET name = 'bboy' WHERE id=1 "
    cursor.execute(sql)
    conn.commit()

    cursor.execute("select * from user")
    print(cursor.fetchall())

    cursor.execute("DELETE FROM user WHERE id=1")
    conn.commit()

    cursor.execute("select * from user")
    print(cursor.fetchall())

    cursor.close()
finally:
    conn.close()


