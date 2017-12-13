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

msg_dic = {}
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
            #所以要想实现这个客户端发数据来时server端能知道，就需要让select监听这个conn
            msg_dic[conn] = queue.Queue()#初始化一个队列，后面存返回给这个客户端的数据
        else:
            data = r.recv(1024)
            print("收到数据",data)
            msg_dic[r].put(data)

            outputs.append(r)#放入返回的连接队列里
            # r.send(data)
            # print("send done...")

    for w in writeable:#要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)#返回给客户端源数据

        outputs.remove(w)#确保下次循环的时候writeable,不返回已经处理完的数据

    for e in exceptional:
        if e in outputs:
            outputs.reverse(e)
        inputs.reverse(e)

        del msg_dic[e]