#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/25 17:31.

import os

print("Process %s running..."% os.getpid())

pid = os.fork()
print(pid)

# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))