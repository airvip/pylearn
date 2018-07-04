#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='root',
                       db='test',
                       charset='utf8')

try:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        res = cursor.fetchall()
        print(res)

    with conn.cursor() as cursor:
        sql = "UPDATE user SET name = %s WHERE id = %s"
        cursor.execute(sql, ('bboy', 1))
    conn.commit()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        res = cursor.fetchall()
        print(res)

    with conn.cursor() as cursor:
        sql = "DELETE FROM user WHERE id = %s"
        cursor.execute(sql, (1))
    conn.commit()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        res = cursor.fetchall()
        print(res)

finally:
    conn.close()

