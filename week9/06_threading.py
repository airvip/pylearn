#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/27 0:20.

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    print("task done", n, threading.current_thread())

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)#把当前线程设置成守护线程
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("all threads has finished".center(50,"*"),threading.current_thread(),threading.active_count())
print("cost:",time.time() - start_time)



