#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
修改
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
coll = testdb['user']

where = {'age': '25'}
fields = {'$set': {'age': 26}}
coll.update_one(where, fields)

for x in coll.find():
    print(x)

