#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/1 0:39.

from multiprocessing import Process,Queue



def f(q):
    q.put([42,None,"hello"])

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
