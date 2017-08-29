#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/27 0:20.

import threading
import time

def run(n):
    lock.acquire()
    global num
    num += 1
    # time.sleep(1)
    lock.release()


lock = threading.Lock()
num = 0
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("all threads has finished".center(50,"*"),threading.current_thread(),threading.active_count())

print("num:",num)



