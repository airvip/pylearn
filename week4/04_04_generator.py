#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 0:43.


import time

def consumer(name):
    print("%s ready eat baozi" %name)
    while True:
        baozi = yield

        print("baizi [%s] comed,eates by [%s]" %(baozi,name))

# c = consumer("yaya")
# c.__next__()
# b1="egg baozi"
# c.send(b1)
# c.__next__()
# c.__next__()

def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print("%s ready make baozi" %name)
    for i in range(10):
        time.sleep(0.3)
        print("make 2 baozis")
        c1.send(i)
        c2.send(i)

producer('airvip')