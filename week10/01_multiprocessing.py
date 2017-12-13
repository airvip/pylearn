#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/31 23:56.

import multiprocessing
import time
import threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print("hello",name)
    t = threading.Thread(target=thread_run)
    t.start()

if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=run,args=("word",))
        p.start()
        # p.join()
