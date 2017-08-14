#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 14:27.

import shelve,datetime

d = shelve.open(r"shelve_learn")

print(d.get("test"))
print(d.get("info"))
print(d.get("date"))

'''
class Test(object):
    def __init__(self,n):
        self.n = n

t = Test(123)
t2 = Test(123334)

info = {"age":23,"job":"it"}

name = ["airvip","rain","learn"]
d["test"] = name#持久化列表
d["info"] = info #持久化dict
d["date"] = datetime.datetime.now()
#d["t1"] = t#持久化类
#d["t2"] = t2
'''
d.close()
