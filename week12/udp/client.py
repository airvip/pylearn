#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename client.py
# 客户端简单实现

#引入socket模块
import socket
#生成socket连接对象client
#AF_INET： 表示使用 IPv4 协议，AF_INET6：表示使用 IPv6协议
#SOCK_DGRAM：表示使用面向数据报的 UDP 协议
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#并没有像 TCP 那样先建立连接，UDP 是直接发送数据
client.sendto('我是阿尔维奇'.encode('utf-8'), ('127.0.0.1', 6969))
#如果服务器有响应内容，我们可以进行接收，如果内容很多也可以进行多次接收
#参数是接受的最大字节数量
data = client.recv(1024)
#打印服务器端响应的数据
print('receice data:',data.decode('utf-8'))
#打印服务器端响应的数据
client.close()