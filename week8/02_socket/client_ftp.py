#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/21 16:29.
import hashlib
import socket,os,time

client = socket.socket()

client.connect(('localhost',9966))

while True:
    cmd = input(">>$").strip()
    if len(cmd) == 0:continue
    if cmd.startswith("get"):
        client.send(cmd.encode("utf-8"))
        server_response = client.recv(1024)
        print("server response:",server_response.decode("utf-8"))
        client.send("ready to recv file".encode("utf-8"))
        file_totle_size =int(server_response.decode("utf-8"))
        receive_size = 0
        _md5 = hashlib.md5()
        file_name = cmd.split()[1]
        f = open(file_name+".copy","wb")
        while receive_size < file_totle_size:
            if file_totle_size - receive_size > 1024:#receive more
                size = 1024
            else:#last time receive all
                size = file_totle_size - receive_size
                print("last receive",size)
            data = client.recv(size)
            _md5.update(data)
            receive_size += len(data)
            f.write(data)
            # print(receive_size,file_totle_size)
        else:
            f.close()
            new_file_md5 = _md5.hexdigest()
            print("file receive over",receive_size,file_totle_size)
        server_file_md5 = client.recv(1024)
        print("server file md5:",server_file_md5.decode("utf-8"))
        print("client file md5:",new_file_md5)


client.close()