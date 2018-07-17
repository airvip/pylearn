#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import multiprocessing
import time

def get_baidu():
    s = requests.get('https://www.baidu.com/')
    print(s)




if __name__ == "__main__":

    start_time = time.time()
    for i in range(10):
        i = multiprocessing.Process(target=get_baidu)
        i.start()

    end_time = time.time()
    print('多进程并行调用耗时 %s 秒' % (end_time-start_time))

