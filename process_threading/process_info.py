#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process, Queue
import random
import time
import os

def p_write(name):
    print("子进程开始工作, ID 为：%s" % os.getpid())
    for value in ['python', 'go', 'php']:
        print('将 %s 放入队列' % value)
        name.put(value)
        time.sleep(random.random())


if __name__ == '__main__':
    q = Queue() # queue不是直接导入的import Queue,这个是 multiprocessing 重新封装的
    p = Process(target=p_write, args=(q,))
    p.start() # 启动
    p.join() # 等待子进程完毕后在继续执行

    for i in range(q.qsize()):
        print(q.get())