#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/4 21:55.

import time
import queue
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)
    gr1.switch()

gr1 = greenlet(test1)#启动一个携程
gr2 = greenlet(test2)
gr1.switch()

