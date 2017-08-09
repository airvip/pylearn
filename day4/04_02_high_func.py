#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 16:01.
import time

def bar():
    time.sleep(1)
    print("in the bar")

def test1(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("the func run time is %s" %(end_time-start_time))

test1(bar)