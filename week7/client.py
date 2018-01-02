#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/2 17:02.


import socket
#生成socket连接对象client
#AF_INET： 表示使用 IPv4 协议，AF_INET6：表示使用 IPv6协议
#SOCK_STREAM：表示使用面向数据流的 TCP 协议
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#现在已经有了链接对象client,要与谁链接，毫无疑问，是服务器端，那就需要知道服务器端 地址及端口号
#注意，下面的参数地址是一个 tuple,包含地址与端口号
client.connect(('localhost',6969))
#已经建立了连接，就需要和服务器沟通了，发送沟通的内容信息
#注意发送的内容类型是字节
client.send("我是阿尔维奇".encode("utf-8"))
#如果服务器有响应内容，我们可以进行接收，如果内容很多也可以进行多次接收
#参数是接受的最大字节数量
data = client.recv(1024)
#打印服务器端响应的数据
print("recive data：",data.decode())
#记住关闭连接
client.close()

