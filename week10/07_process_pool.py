#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/3 23:09.

from multiprocessing import Process,Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i+100

def Bar(arg):
    print("-->exec done:",arg,os.getpid())


if __name__ == "__main__":#此句就是手动调用就执行下面的语句，当作模块就不执行
    #freeze_support()#for windows
    pool = Pool(processes=5)#允许进程池中同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#callback 回掉
        # pool.apply(func=Foo,args=(i,))#串行
        # pool.apply_async(func=Foo,args=(i,))#异步 并行

    print('end')
    pool.close()

    #进程池中进程执行完毕后在关闭，如果注释掉，那么程序直接关闭
    #先关闭后join
    pool.join()