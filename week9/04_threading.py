#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/26 23:51.

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    print("task over",n)


start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()

print("cost:",time.time() - start_time)