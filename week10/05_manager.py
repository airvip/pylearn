#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/2 2:23.

from multiprocessing import Process,Pipe,Manager
import os

def f(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid())
    print(l)

if __name__ == "__main__":
    with Manager() as manager:
        #生成一个字典，可在多个进程中共享和传递
        d = manager.dict()
        l = manager.list(range(5))#生成一个列表，可在多个进程中共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:#wait result
            res.join()

        print(d)
        print(l)