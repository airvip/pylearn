#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/30 23:23.


import queue
#first in first out

q = queue.Queue()

q.put("airvip1")
q.put("airvip2")
q.put("airvip3")

print(q.get())
print(q.get())
print(q.get())