#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/31 22:28.

import queue

#
q = queue.PriorityQueue()

q.put((1,"airvip"))
q.put((2,"airvip2"))
q.put((-1,"airvip3"))
q.put((-6,"airvip4"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())