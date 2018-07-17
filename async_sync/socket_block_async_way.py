#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import socket
import time

def no_blocking_way():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    try:
        client.connect(('115.239.211.112', 80))
    except BlockingIOError:
        pass # 非阻塞链接抛出异常

    requests = 'GET / HTTP/1.0\r\n Host:www.baidu.com\r\n\r\n'.encode('uft-8')
    while True:
        pass


