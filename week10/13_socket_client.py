#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/4 23:47.


import socket

HOST = "localhost"
PORT = 5050
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:"),encoding="utf-8")
    s.sendall(msg)
    data = s.recv(1024)

    print("Received",repr(data))

s.close()