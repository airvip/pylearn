#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/21 16:29.

import socket,os

server = socket.socket()
server.bind(('localhost',9966))

server.listen()

while True:
    conn,addr = server.accept()
    print("new conn",addr)
    while True:
        print("wait instructions")
        data = conn.recv(1024)
        if not data:
            print("client has break...")
            break
        print("excutive instruction",data.decode("utf-8"))
        cmd_res = os.popen(data.decode("utf-8")).read()#popen接收字符串，执行结果也是字符串
        print("send before",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(str(len(cmd_res)).encode("utf-8"))
        # 如果发生粘包
        # time.sleep(0.5)
        client_ack = conn.recv(1024)
        print("now send instructions data")
        conn.send(cmd_res.encode("utf-8"))
        print("send after")

server.close()