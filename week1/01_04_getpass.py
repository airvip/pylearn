#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 9:59.

import getpass
_username = 'airvip'
_password = '123456'

username = input("username:")
password = getpass.getpass("password:")
#print(username,password)
if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password.")

