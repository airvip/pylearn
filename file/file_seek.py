#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/2 11:12.

f = open("ff.txt", "r+")
print("文件名:%s" % f.name)

line = f.readline()
print(line)

f.seek(3, 0)
line = f.readline()
print(line)

f.write('\r\nthis is 5th line')
data = f.read()
print(data)

f.close()