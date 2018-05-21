#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time


def thread_run():
    n = 0
    for i in range(100000000):
        n = i + 1
    return n

if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=thread_run)
    t2 = threading.Thread(target=thread_run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print("总共用时: {}".format(end_time - start_time))