#!/usr/bin/env python3
# -*- coding:utf-8 -*-

list1 = [1, 2, 3]
print(locals())
print(locals()['list1'])

def foo(args):
    name = 'airvip'
    print(locals())
    print(locals()[args])

foo('name')

