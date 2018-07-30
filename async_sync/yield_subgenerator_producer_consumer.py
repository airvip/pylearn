#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time


def eat():
    print("老板上包子")
    bao = ''
    while True:
        baozi = yield bao
        print("[消费者]-吃 %s" % (baozi))
        time.sleep(0.1)

def consumer():
    geat = eat()
    bao = None
    res = geat.send(bao)
    while True:
        try:
            bao = yield res
            res = geat.send(bao)
        except StopIteration:
            break
        except Exception as err:
            try:
                res = geat.throw(err)
            except StopIteration:
                break




def producer(c):
    c.send(None)
    n = 0
    while n < 10:
        n += 1
        print("[生产者]-生产第 %s 个包子"%n)
        c.send("包子 {}".format(n))
    c.close()


producer(consumer())

