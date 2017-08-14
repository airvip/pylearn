#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 18:29.

str = "我爱北京天安门"
print(str)
print(str.encode())
print(str.encode('utf-8'))
print(str.encode('utf-8').decode())
print(str.encode('utf-8').decode('utf-8'))