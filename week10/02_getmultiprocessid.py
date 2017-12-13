#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/1 0

from multiprocessing import Process
import os

def info(title):
    print(title)
    print("module name:",__name__)
    print("parent process:",os.getppid())
    print("process id:",os.getpid())
    print("\n\n")


def f(name):
    info("\033[31;1mcall from child process function f\033[0m")
    print("hello",name)

if __name__ == "__main__":
    info("\033[32;1mmain process line\033[0m ")
    p = Process(target=f,args=("bob",))
    p.start()
    p.join()