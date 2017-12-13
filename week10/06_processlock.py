#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/3 22:59.

from multiprocessing import Process,Lock


def f(lock,num):
    lock.acquire()
    try:
        print("hello word",num)
    finally:
        lock.release()


if __name__ == "__main__":
    lock = Lock()

    for num in range(10):
        Process(target=f,args=(lock,num)).start()
