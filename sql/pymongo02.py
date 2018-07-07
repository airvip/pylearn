#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
查询数据
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
coll = testdb['user']

for x in coll.find():
    print(x)

