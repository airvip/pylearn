#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import socket
import time

def blocking_way():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('www.baidu.com', 80))
    requests = 'GET / HTTP/1.1\r\n Host:www.baidu.com\r\nConnection: close\r\n\r\n'.encode('utf-8')
    client.send(requests)

    res = b''
    slice_res = client.recv(2048)
    while slice_res:
        res += slice_res
        # 阻塞接收
        slice_res = client.recv(2048)

    print(len(res.decode('utf-8')))
    client.close()


if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        blocking_way()
    end_time = time.time()
    print('同步阻塞调用耗时 %s 秒' % (end_time - start_time))



