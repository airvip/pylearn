#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/2 17:20.

from multiprocessing import Pool
import random
import time
import os

def p_run1(name):
    print("p1 %s 号子进程开始工作, ID 为：%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()) # 随机休息一点时间
    end = time.time()
    print("p1 %s 号子进程用时 %.3f 秒" % (name, (end - start)))

def p_run2(name):
    print("p2 %s 号子进程开始工作, ID 为：%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random(1,3)) # 随机休息一点时间
    end = time.time()
    print("p2 %s 号子进程用时 %.3f 秒" % (name, (end - start)))

if __name__ == '__main__': # 在交互式模式下自动执行
    start = time.time()
    print("父进程 ID 为 %d" % os.getpid())
    p = Pool(3)
    for fun in [p_run1,p_run2]:
        for i in range(4):
            p.apply_async(fun, args=(i,))
    p.close()
    p.join()
    end = time.time()
    print("所有子进程执行结束, 用时 %.3f" % (end - start))