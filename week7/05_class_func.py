#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 17:59.

#普通方式创建类
class Foo(object):
    def __init__(self,name):
        self.name = name


f = Foo("air")
print(type(f))
print(type(Foo))


#装逼方式创建类
def func(self):
    print("hello world | airvip")

Foo = type('Foo',(),{'func':func})
print(type(Foo))
# Foo1 = type('Foo1',(object),{'func':func})
# print(type(Foo1))

f = Foo()
f.func()