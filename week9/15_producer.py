#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/31 22:36.

import threading,time
import queue

q = queue.Queue(10)

def Producer(name):
    count = 1
    while True:
        q.put("gu tou %s"%count)
        print("make gutou %s"%count)
        count +=1
        time.sleep(0.2)


def Consumer(name):
    while True:
        print("[%s] get [%s] and eating..."%(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("airvip",))
c = threading.Thread(target=Consumer,args=("niuniu",))
c1 = threading.Thread(target=Consumer,args=("yaya",))

p.start()
c.start()
c1.start()

