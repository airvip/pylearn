#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

try:
    cursor =conn.cursor()

    cursor.execute("select * from user")
    print(cursor.fetchall())

    sql = "INSERT INTO `user` (`id`, `name`) VALUES (1, 'airivp') "
    cursor.execute(sql)
    conn.commit()

    cursor.execute("select * from user")
    print(cursor.fetchall())
finally:
    conn.close()


