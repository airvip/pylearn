#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time

def get_baidu():
    s = requests.get('https://www.baidu.com/')
    print(s)



if __name__ == "__main__":

    start_time = time.time()
    for i in range(10):
        get_baidu()

    end_time = time.time()
    print('同步阻塞调用耗时 %s 秒' % (end_time-start_time))

