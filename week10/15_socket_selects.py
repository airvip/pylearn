#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/9 15:06.

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()#should be ready
    print("accepred",conn,"from",addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)
    # pass


def read(conn,mask):
    data = conn.recv(1024)#should be ready
    if data:
        print("echoing",repr(data),"to",conn)
        conn.send(data)#hope it won't block
    else:
        print("closing",conn)
        sel.unregister(conn)
        conn.close()
    # pass


sock = socket.socket()
sock.bind(('localhost',5050))
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)

while True:
    events = sel.select()#默认阻塞，有活动链接就返回活动的连接列表
    for key,mask in events:
        callback = key.data#accept
        callback(key.fileobj,mask)#key.fileobj = 文件句柄


