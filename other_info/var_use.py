#!/usr/bin/env python3
# -*- coding:utf-8 -*-

list1 = [1, 2, 3]
print(vars())
print(vars()['list1'])


class Foo(object):
    name = 'airvip'


print(Foo)
foo = Foo
print(vars(foo))
print(vars(foo)['name'])


class People(object):

    age = 17

    def __init__(self, name):
        name = name


print(People)
p = People
print(vars(p))


