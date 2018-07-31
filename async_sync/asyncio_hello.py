#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio

@asyncio.coroutine
def hello(t):
    print('Start Hello %s' %t)
    yield from asyncio.sleep(t) #  表示不同时间的IO操作
    print('End Hello %s' %t)

# 获取 EventLoop
loop = asyncio.get_event_loop()
tasks = [hello(3), hello(2)]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()