#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/18 18:03.

import socket
#客户端
client = socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

client.send(b"Hello World!")
data = client.recv(1024)
print("recive data",data)

client.close()