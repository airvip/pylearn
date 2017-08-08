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


def test2(*args):
    print(args)
test2(1,2,3,4,5)
test2(*[1,2,3,4,5])

def test3(x,*args):
    print(x)
    print(args)
test3(1,2,3,4,5)
test3(*[1,2,3,4,5])

def test4(**kwargs):
    print(kwargs)
test4(name="airvip",age="21",sex="F")
test4(**{"name":"airvip","age":"21","sex":"F"})

def test5(name,**kwargs):
    print(name)
    print(kwargs)
test5("airvip",age="21",sex="F")
test5("airvip",**{"age":"21","sex":"F"})
'''
def test6(name,age=12,**kwargs):
    print(name)
    print(age)
    print(kwargs)
test6("airvip",love="pp",sex="F")
test6("airvip",love="pp",sex="F",age=18)
test6("airvip",**{"age":"21","sex":"F"})