#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/18 18:03.

import socket
#客户端
client = socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

# client.send(b"Hello World!")
client.send("我是阿尔维奇".encode("utf-8"))
data = client.recv(1024)
print("recive data：",data.decode())

client.close()