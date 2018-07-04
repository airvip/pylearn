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
        cursor.execute("SHOW TABLES")
        tag = True
        for t in cursor.fetchall():
            if 'user' in t:
                tag = False
                break

        if tag:
            sql = "CREATE TABLE IF NOT EXISTS user (" \
                  "id INT(10) NOT NULL AUTO_INCREMENT , " \
                  "name VARCHAR(20) NOT NULL DEFAULT ''," \
                  "PRIMARY KEY (id)" \
                  ") ENGINE=InnoDB"
            cursor.execute(sql)

        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())
finally:
    conn.close()

