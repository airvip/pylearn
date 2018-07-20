#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import selectors
import time

sel = selectors.DefaultSelector()
tag = 1

class Future(object):
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

class Callnext(object):
    def __init__(self):
        self.res = b''

    def accept(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.setblocking(False)
        try:
            conn.connect(('115.239.211.112', 80))
        except BlockingIOError:
            pass

        f = Future()
        def on_connected():
            f.set_result(None)

        sel.register(conn, selectors.EVENT_WRITE, on_connected)
        yield f
        sel.unregister(conn)

        requests = 'GET / HTTP/1.1\r\n Host:www.baidu.com\r\nConnection: close\r\n\r\n'.encode('utf-8')
        conn.send(requests)

        global tag
        while tag:
            f = Future()

            def read_response():
                f.set_result(conn.recv(2048))

            sel.register(conn, selectors.EVENT_READ, read_response)
            slice_res = yield f
            sel.unregister(conn)
            if slice_res:
                self.res += slice_res
            else:
                tag -= 1
                print(len(self.res.decode('utf-8')))
                conn.close()
                break

class Task(object):
    def __init__(self, conn):
        self.conn = conn
        f = Future()
        self.step(f)

    def step(self, future):
        try:
            # send 会进入到 conn 执行, 即:accept, 直到下次 yield
            # next_future 为 yield 返回的对象
            # 第一次启动 future.result 为 None
            next_future = self.conn.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(tag):
        call = Callnext()
        Task(call.accept())

    while tag:
        # 一直阻塞, 直到一个事件发生
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback()

    end_time = time.time()
    print('yeild调用耗时 %s 秒' % (end_time - start_time))