#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/1 11:47.

from multiprocessing import Process
import time
import os

# 定义子进程执行的的内容
def p_run(name):
    print("我是子进程 %s, ID 为：%d" % (name, os.getpid()))

if __name__=='__main__':
    a = time.time()
    print("当前的进程(父进程) ID 为：%d" % os.getpid())
    # 创建Process的实例，并传入子线程要执行的函数和参数
    proc = Process(target=p_run, args=('test',))
    # 子进程开始执行
    proc.start()
    # join方法用于进程间的同步，等子进程执行完毕后再往下执行
    proc.join()
    print("子进程执行结束, 回到主进程：%d, 用时 %s" % (os.getpid(), time.time() - a))


