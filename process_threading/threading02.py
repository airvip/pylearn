#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import _thread
import time
import random

# 线程要执行的函数
def thread_run(name):
    for i in range(3):
        start_time = time.time()
        time.sleep(random.random())
        end_time = time.time()
        print("%s %s 执行，用时 %.4f" % ( name, i, end_time-start_time ))

if __name__ == '__main__':
    start_time = time.time()
    print("默认开启的线程开始执行")
    # 创建两个线程
    try:
        _thread.start_new_thread(thread_run, ("Thread-01",))
        _thread.start_new_thread(thread_run, ("Thread-02",))
    except:
        print("线程启动失败")
    end_time = time.time()
    print("默认开启的线程结束执行,共用时 %.4f" % (end_time - start_time))

    time.sleep(2)

