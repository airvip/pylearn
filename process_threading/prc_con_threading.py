#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading, time
import queue

q = queue.Queue(10)

def Producer():
    count = 1
    while True:
        q.put("包子 %s"%count)
        print("[生产者]-生产第 %s 个包子"%count)
        count +=1
        time.sleep(0.2)


def Consumer():
    while True:
        print("[消费者]-吃 %s"%(q.get()))
        time.sleep(0.1)

p = threading.Thread(target=Producer)
c = threading.Thread(target=Consumer)

p.start()
c.start()

