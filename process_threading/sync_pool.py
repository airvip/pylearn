#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/2 17:06.

from multiprocessing import Pool
import random
import time
import os

def p_run(name):
    print("%s 号子进程开始工作, ID 为：%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()) # 随机休息一点时间
    end = time.time()
    print("%s 号子进程用时 %.3f 秒" % (name, (end - start)))

if __name__ == '__main__': # 在交互式模式下自动执行
    start = time.time()
    print("父进程 ID 为 %d" % os.getpid())
    p = Pool(3)
    for i in range(4):
        # apply方法(阻塞)，传入子进程要执行的函数和函数参数(以元组的形式)
        p.apply(p_run, args=(i,))
    p.close() # 关闭pool,不能再添加新的任务
    p.join()
    end = time.time()
    print("所有子进程执行结束, 用时 %.3f" % (end - start))