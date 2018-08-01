#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
import threading

@asyncio.coroutine
def hello(t):
    print('Start Hello %s, Threading Pid: %s' % (t, threading.current_thread().ident))
    yield from asyncio.sleep(t) #  表示不同时间的IO操作
    print('End Hello %s, Threading Pid: %s' % (t, threading.current_thread().ident))

# 获取 EventLoop
loop = asyncio.get_event_loop()
tasks = [hello(3), hello(2)]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(asyncio.gather (*[asyncio.ensure_future(i) for i in tasks] ))
loop.run_until_complete(asyncio.gather (hello(3), hello(2)))
loop.close()
