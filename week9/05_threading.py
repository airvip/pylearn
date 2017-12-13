#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/27 0:08.

import threading
import time

class MyThread(threading.Thread):

    def __init__(self,n,sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print("running task",self.n)
        time.sleep(self.sleep_time)
        print("task%s done"%self.n)

t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join() # =wait()
t2.join() # =wait()
print("main thread...")
