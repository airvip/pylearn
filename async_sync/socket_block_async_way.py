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

    requests = 'GET / HTTP/1.1\r\n Host:www.baidu.com\r\nConnection: close\r\n\r\n'.encode('utf-8')

    while True: # 由于不知链接何时成功建立，一直尝试发送
        try:
            client.send(requests) # 直到send不抛异常，则发送完成
            break
        except OSError:
            pass

    res = b''
    while True: # 由于不知道何时发送请求成功，一直尝试接收
        try:
            slice_res = client.recv(2048)
            while slice_res:
                res += slice_res
                slice_res = client.recv(2048)
            break
        except OSError:
            pass

    print(len(res.decode('utf-8')))
    client.close()



if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        no_blocking_way()
    end_time = time.time()
    print('非阻塞调用耗时 %s 秒' % (end_time - start_time))