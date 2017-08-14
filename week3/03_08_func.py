#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/8 9:43.

def test1():
    print("in the test1")

def test2():
    print("in the test2")
    return 0

def test3():
    print("in the test3")
    return 1,"hello",['a',"b"],{"name":"airvip"}

x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)