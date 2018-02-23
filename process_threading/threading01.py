#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time
import random

# 线程要执行的函数
def thread_run():
    print('子线程 %s 开始执行' % threading.current_thread().name)
    for i in range(3):
        start_time = time.time()
        time.sleep(random.random())
        end_time = time.time()
        print("%s >>> %s 执行，用时 %.4f" % ( threading.current_thread().name, i, end_time-start_time ))
    print('子线程 %s 结束运行' % threading.current_thread().name)


if __name__ == '__main__':
    print('线程 %s 开始运行' % threading.current_thread().name)
    t1 = threading.Thread(target=thread_run, name='ThreadSon1')
    t1.start()

    t2 = threading.Thread(target=thread_run, name='ThreadSon2')
    t2.start()

    t1.join()
    t2.join()
    print('线程 %s 结束运行' % threading.current_thread().name)
