#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 15:11.


# def foo():
#     print("in the foo")
#     bar()
# foo()

def bar():
    print("in the bar")

def foo():
    print("in the foo")
    bar()
foo()

calc = lambda x:x*3
print(calc(3))