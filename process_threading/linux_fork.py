#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# only in Unix/Linux/Mac

import os

print("当前的进程 ID 为 ：%s " % os.getpid()) # os.getpid()返回的是进程的id
# PID : 一个非负整型表示的唯一进程ID
PID = os.fork() # 创建子进程，并返回进程的id，父进程返回的是子进程的id，子进程返回的是0

if 0 == PID:
    print('我是子进程，ID 为 (%s)，父进程 ID 为 (%s)' % (os.getpid(), os.getppid()))
else:
    print('我是父进程，ID 为 (%s)，创建了一个 ID 为 (%s) 的子进程' % (os.getpid(), PID))