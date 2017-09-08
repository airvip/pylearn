#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/8 23:48.


import select
import socket
import sys
import Queue

#create TCP/IP socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)


#bind the socket to the port
server_address = ("localhost",9696)
print(">>"+sys.stderr,"starting up on %s port %s" %(server_address))
server.bind(server_address)

#Listen for incoming connections
server.listen(5)