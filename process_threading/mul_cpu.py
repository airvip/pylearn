#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import multiprocessing
import threading
import time
import random


def p_run(name):
    for i in range(3):
        start_time = time.time()
        time.sleep(random.random())
        end_time = time.time()
        print("%s 执行，用时 %.4f" % (i, end_time-start_time ))

if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpu_count)
    for i in range(4):
        # apply_async方法(非阻塞)，传入子进程要执行的函数和函数参数(以元组的形式)
        p.apply_async(p_run, args=(i,))
    p.close() # 关闭pool,不能再添加新的任务
    p.join()
