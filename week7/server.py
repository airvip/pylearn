#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/2 17:02.

import socket
#生成socket连接对象client
#AF_INET： 表示使用 IPv4 协议，AF_INET6：表示使用 IPv6协议
#SOCK_STREAM：表示使用面向数据流的 TCP 协议
#服务器端要与协议一致
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定要监听的地址
#注意，下面的参数地址是一个 tuple,包含地址与端口号
server.bind(('localhost',6969))
#进行监听，参数是这个服务可以接收的连接数
server.listen(1)
#打印说明信息
print("我想被连接，我在等待")
#等待连接
conn,addr = server.accept()
data = conn.recv(1024)
print("recive:",data.decode())
conn.send(data.upper())
#关闭连接
server.close()