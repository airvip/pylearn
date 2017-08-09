#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 15:11.


import time

def bar():
    time.sleep(1)
    print("in the bar")

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)
bar()