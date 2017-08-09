#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 15:11.

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper


@timmer
def test1():
    time.sleep(3)
    print("in the tes1")

test1()