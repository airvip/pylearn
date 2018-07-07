#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

'''
删除
'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
testdb = myclient["test"]
coll = testdb['user']

coll.drop()

