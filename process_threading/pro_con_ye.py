#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

def consumer():
    print("老板上包子")
    bao = ''
    while True:
        baozi = yield bao
        print("[消费者]-吃 %s"%(baozi))
        time.sleep(0.1)
        bao = baozi

def producer(c):
    c.send(None)
    n = 0
    while n < 10:
        n += 1
        print("[生产者]-生产第 %s 个包子"%n)
        bao = c.send("包子 {}".format(n))
        print("顾客说 %s 吃完了" % bao)
    c.close()

c = consumer()
producer(c)