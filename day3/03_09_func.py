#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/8 9:55.

'''
#位置参数要在关键字参数之前
def test(x,y,z):
    print(x)
    print(y)
    print(z)

test(1,2,3)
test(1,2,z=3)
test(1,y=2,z=3)
test(1,z=3,y=2)

def test1(x,y=2):
    print(x)
    print(y)
'''
def test2(*arg):
    print(arg)


test2(1,2,3,4,5)
