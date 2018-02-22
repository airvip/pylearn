#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process, Queue
import random
import time
import os

def p_write(name):
    print("写子进程开始工作, ID 为：%s" % os.getpid())
    for value in ['python', 'go', 'php']:
        print('将 %s 放入队列' % value)
        name.put(value)
        time.sleep(random.random())

def p_read(name):
    print("读子进程开始工作, ID 为：%s" % os.getpid())
    for i in range(name.qsize()):
        print('在队列中读取到 %s' % name.get())

if __name__ == '__main__':
    q = Queue() # queue不是直接导入的import Queue,这个是 multiprocessing 重新封装的
    pw = Process(target=p_write, args=(q,))
    pw.start() # 写子进程启动
    pw.join() # 等待子进程完毕后在继续执行

    pr = Process(target=p_read, args=(q,))
    pr.start()  # 读子进程启动
    pr.join() # 等待子进程完毕后在继续执行

