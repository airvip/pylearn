#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/4 21:55.

import gevent

def foo():
    print("running in foo")
    gevent.sleep(2)
    print("Explicit context switch to foo again")

def bar():
    print("explicit context to bar foo")
    gevent.sleep(1)
    print("Implicit context switch to bar")

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),

])