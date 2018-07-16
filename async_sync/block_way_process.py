#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import multiprocessing
import time

def blocking_way():
    s = requests.get('https://www.baidu.com/')
    return s



if __name__ == "__main__":

    start_time = time.time()
    cpu_count = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpu_count)
    for i in range(4):
        # apply_async方法(非阻塞)，传入子进程要执行的函数和函数参数(以元组的形式)
        p.apply_async(blocking_way)
    p.close()  # 关闭pool,不能再添加新的任务
    p.join()

    end_time = time.time()
    print('多进程调用耗时 %s 秒' % (end_time-start_time))

