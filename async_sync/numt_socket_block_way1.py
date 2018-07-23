#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import socket
import time
from concurrent import futures

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
    with futures.ThreadPoolExecutor(10) as executor:
        for i in range(10):
            executor.submit(blocking_way)
    end_time = time.time()
    print('多线程并行调用耗时 %s 秒' % (end_time - start_time))



