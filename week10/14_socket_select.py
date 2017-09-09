#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/8 23:48.


import select
import socket
import sys
import queue

#create TCP/IP socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind the socket to the port
server_address = ("localhost",5050)
# print(sys.stderr,"starting up on %s port %s" %(server_address))
server.bind(server_address)
#Listen for incoming connections
server.listen(5)


server.setblocking(0)#设置不阻塞

inputs = [server,]
# inputs = [server,conn]
outputs = []
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptional)
    # server.accept()
    for r in readable:
        if r is server:#代表来了一个新链接
            conn,addr = server.accept()
            print("来了一个新链接",addr)
            inputs.append(conn)#因为新建立的连接还没有发数据过来，现在接数据的程序就报错
        else:
            data = r.recv(1024)
            print("收到数据",data)
            r.send(data)
            print("send done...")