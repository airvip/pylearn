#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/21 16:29.

import socket,os

client = socket.socket()

client.connect(('localhost',9966))

while True:
    cmd = input(">>$").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)#接收命令结果的长度
    print("instructions result size:",cmd_res_size)
    receive_size = 0
    # receive_data = b''
    print(cmd_res_size.decode())
    while receive_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        receive_size += len(data.decode("utf-8"))#每次收到的有可能小于1024，所以必须用len判断
        print(data.decode("utf-8"))
        # print(len(data))
    else:
        print("cmd res receive done...",receive_size)
    # cmd_res = client.recv(1024)
    # print(cmd_res.decode("utf-8"))

client.close()