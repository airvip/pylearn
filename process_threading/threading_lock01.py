#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time
import random

my_zero = 0

# 线程要执行的函数
def thread_run(n):
    for i in range(2):
        global my_zero  # 多线程是共享资源的，使用全局变量
        my_zero = my_zero + n
        print("%s + 操作， zero 值是 %d" % (threading.current_thread().name, my_zero))
        time.sleep(random.random())
        my_zero = my_zero - n
        print("%s - 操作， zero 值是 %d" % (threading.current_thread().name, my_zero))


if __name__ == '__main__':
    print('zero 初始值 %d' % my_zero)
    t1 = threading.Thread(target=thread_run, name='ThreadSon1',args=(2,))
    t2 = threading.Thread(target=thread_run, name='ThreadSon2',args=(3,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('zero 最终值 %d' % my_zero)