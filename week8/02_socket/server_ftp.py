#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/21 16:29.
import hashlib
import socket,os,time

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
        cmd,filename = data.decode("utf-8").split()
        print(filename)
        if os.path.isfile(filename):
            f =open(filename,"rb")
            _md5 = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode("utf-8"))#send file size
            conn.recv(1024)#wait for ack
            for line in f:
                _md5.update(line)
                conn.send(line)
            print("file md5",_md5.hexdigest())
            f.close()
            conn.send(_md5.hexdigest().encode())

        print("send over")

server.close()