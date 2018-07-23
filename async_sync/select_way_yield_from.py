#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import selectors
import time

sel = selectors.DefaultSelector()
tag = 10

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

    def __iter__(self):
        yield self
        return self.result

def to_connect(sock, addr):
    sock.setblocking(False)
    try:
        sock.connect(addr)
    except BlockingIOError:
        pass

    f = Future()
    def on_connected():
        f.set_result(None)

    sel.register(sock, selectors.EVENT_WRITE, on_connected)
    yield from f
    sel.unregister(sock)

def read(sock):
    f = Future()

    def readable():
        f.set_result(sock.recv(2048))

    sel.register(sock, selectors.EVENT_READ, readable)
    slice_res = yield from f
    sel.unregister(sock)
    return slice_res

def read_all(sock):
    reponse = b''
    slice_res = yield from read(sock)
    while slice_res:
        reponse += slice_res
        slice_res = yield from read(sock)
    return  reponse


class Callbaidu(object):
    def __init__(self):
        self.res = b''

    def accept(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        yield from to_connect(sock, ('115.239.211.112', 80))
        requests = 'GET / HTTP/1.1\r\n Host:www.baidu.com\r\nConnection: close\r\n\r\n'.encode('utf-8')
        sock.send(requests)
        self.res = yield from read_all(sock)
        print(len(self.res))

        global tag
        tag -= 1



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
        call = Callbaidu()
        Task(call.accept())

    while tag:
        # 一直阻塞, 直到一个事件发生
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback()

    end_time = time.time()
    print('yield from调用耗时 %s 秒' % (end_time - start_time))