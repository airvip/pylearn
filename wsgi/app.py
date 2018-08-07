#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'  # HTTP STATUS
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    return ["<b>Hello World</b>".encode('utf-8')]

# 创建一个服务器，IP地址为空，端口是8888，处理函数是 application:
httpd = make_server('', 8888, application)
print('server running:127.0.0.1:8888')
# 直到进程被杀死:
httpd.serve_forever()