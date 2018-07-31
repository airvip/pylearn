#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
import time

@asyncio.coroutine
def hello(t):
    print('Start Hello %s' %t)
    yield from asyncio.sleep(t) #  表示不同时间的IO操作
    print('End Hello %s' %t)

start_time = time.time()
# 获取 EventLoop
loop = asyncio.get_event_loop()
tasks = [hello(3), hello(2)]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end_time = time.time()
print("总共用时: %s"  %(end_time - start_time))