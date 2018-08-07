#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'  # HTTP STATUS
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)
    response_body = '<b>hello {}</b>'.format(environ['PATH_INFO'][1:] or 'world')
    return [response_body.encode('utf-8')]


class Upperware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        for data in self.app(environ, start_response):
            yield data.upper()


app_ware = Upperware(application)
# 创建一个服务器，IP地址为空，端口是8888，处理函数是 application:
httpd = make_server('', 8888, app_ware)
print('server running:127.0.0.1:8888')
# 直到进程被杀死:
httpd.serve_forever()