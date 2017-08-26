#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/27 0:20.

import threading
import time

def run(n):
    print("task done",n)
    time.sleep(2)

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("cost:",time.time() - start_time)



