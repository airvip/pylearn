#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
删除
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
coll = testdb['user']

where = {'name': '阿尔维奇'}
res = coll.delete_many(where)

print(res)
print("删除 %s 个文档" % res.deleted_count)

