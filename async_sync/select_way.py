#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import selectors
import time

sel = selectors.DefaultSelector()
tag = 10

class Callbaidu(object):
    def __init__(self):
        self.conn = None
        self.res = b''

    def accept(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setblocking(False)
        try:
            self.conn.connect(('115.239.211.112', 80))
        except BlockingIOError:
            pass
        sel.register(self.conn, selectors.EVENT_WRITE, self.send)

    def send(self, conn, mask):
        sel.unregister(conn)
        requests = 'GET / HTTP/1.1\r\n Host:www.baidu.com\r\nConnection: close\r\n\r\n'.encode('utf-8')
        conn.send(requests)
        sel.register(conn, selectors.EVENT_READ, self.read_response)

    def read_response(self, conn, mask):
        global tag
        slice_res = conn.recv(2048)

        if slice_res:
            self.res += slice_res
        else:
            sel.unregister(conn)
            tag -= 1
            print(len(self.res.decode('utf-8')))
            conn.close()


if __name__ == '__main__':
    start_time = time.time()
    for i in range(tag):
        call = Callbaidu()
        call.accept()

    while tag:
        # 一直阻塞, 直到一个事件发生
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)  # key.fileobj 就是 send与read_response 中的一个socket连接对象

    end_time = time.time()
    print('callback调用耗时 %s 秒' % (end_time - start_time))