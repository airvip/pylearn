#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 15:11.

#装饰器  嵌套函数  + 高阶函数

import time

def timer(func):
    def deco():
        start_time = time.time()
        func()
        end_time = time.time()
        print("the function run time is %s" %(end_time-start_time))
    return deco

@timer # =timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")

@timer
def test2():
    time.sleep(2)
    print("in the test2")


# test1 = timer(test1)
test1()

#新增功能却修改了调用方式
# deco(test1)
# deco(test2)

# test1()
# test2()