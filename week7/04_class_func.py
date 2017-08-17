#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 17:44.

class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        print("__getitem__",item)
        return self.data.get(item)

    def __setitem__(self, key, value):
        print("__setitem__",key,value)
        self.data[key] = value

    def __delitem__(self, key):
        print("__delitem",key)



obj = Foo()
obj['k2'] = 'airvip'#自动触发执行 __setitem__
print(obj.data)
result = obj['k1']#自动触发执行 __getitem__
print(result)



del obj['k1']