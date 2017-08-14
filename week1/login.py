#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 14:36.


f = open('login.txt','r')
_username = f.readline().strip()
_password = f.readline().strip()
_tag = f.readline().strip()
f.close()

import getpass
count = 0
if _tag:
    print('you has input error three time,this count can not login.')
else:
    for i in range(4):
        if count == 3:
            f = open('login.txt','a')
            f.write('1')
            f.close()
            break
        username = input('username:')
        password = getpass.getpass('password:')
        if _username == username and _password == password:
            print("welcom {username} login... ".format(username=username))
            break
        else:
            print('your username or password is error...')
            count += 1




