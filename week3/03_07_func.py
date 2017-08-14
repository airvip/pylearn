#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/8 9:21.
import time

def log():
    with open("03_07_func","a+",encoding="utf-8") as f:
        time_format = "%Y-%m-%d %X"#time style
        time_current = time.strftime(time_format)

        f.write(("%s end action" %time_current).center(50,"*")+"\n")

def test1():
    print("in the test1")
    log()

def test2():
    print("in the test2")
    log()

def test3():
    print("in the test3")
    log()

test1()
test2()
test3()