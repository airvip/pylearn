#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/31 22:26.

import queue
#last in last out
q = queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)

print(q.get(),q.get(),q.get())