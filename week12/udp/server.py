#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#  filename server.py
# 服务端简单实现

#引入socket模块
import socket
#生成socket连接对象server
#AF_INET： 表示使用 IPv4 协议，AF_INET6：表示使用 IPv6协议
#SOCK_DGRAM：表示使用面向数据报的 UDP 协议
#服务器端要与客户端协议一致
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
server.bind(('127.0.0.1', 6969))
print("服务已经启动")
# 不需要监听，直接接收
data, addr = server.recvfrom(1024)
print('receive from %s:%s.' % (addr,data.decode('utf-8')))
server.sendto(data, addr)
#关闭连接,当然你也可以不关闭
server.close()
