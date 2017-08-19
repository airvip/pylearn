
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/19 17:12.

import socket
#服务器端
server = socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen()#监听

print("i wait connect")
conn,addr = server.accept()#等待连接
print(conn,addr)
print("connect arrived")

data = conn.recv(1024)
print("recive:",data)
conn.send(data.upper())

server.close()