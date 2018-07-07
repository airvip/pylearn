#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
创建数据库就要创建集合并且插入文档
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
print(myclient.list_database_names())

coll = testdb['user']
print(testdb.collection_names())

info = {"name": "阿尔维奇", "age":"25"}
doc = coll.insert_one(info)
print(doc)
print(doc.inserted_id)

print(myclient.list_database_names())
print(testdb.collection_names())
