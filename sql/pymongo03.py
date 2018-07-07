#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
查询指定条件
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
coll = testdb['user']

where = {'age': '25'}
fields = {'_id': 0, 'name': 1, 'age':1}

for x in coll.find(where, fields):
    print(x)

