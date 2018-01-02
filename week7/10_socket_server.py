
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/19 17:12.

import os
import socket
#服务器端
server = socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen(5)#监听

print("i wait connect")
while True:
    conn,addr = server.accept()#等待连接

    #conn 就是客户端连接过来而在服务器为其生成的一个连接实例
    print(conn,addr)
    print("connect arrived")
    count = 0
    while True:
        data = conn.recv(1024)
        print("recive:",data)
        if not data:
            print("client has lost...")
            break
        # res = os.popen(data).read()
        # conn.send(res)
        conn.send(data.upper())
        count +=1
        if count > 10:break


    server.close()