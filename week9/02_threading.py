#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/26 23:40.

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)


t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))
t1.start()
t2.start()