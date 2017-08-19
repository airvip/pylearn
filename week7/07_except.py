#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/18 11:15.

names = ["airvip","yaya"]
data = {}

try:
    names[3]
    data['name']
except KeyError as e:
    print("no have this key:",e)
except IndexError as e:
    print("list opreation error:",e)


try:
    names[3]
    data['name']
except (KeyError,IndexError) as e:
    print("error info:",e)


try:
    names[3]
    data['name']
except Exception as e:
    print("error info:",e)
else:
    print("all right")
finally:
    print("ok or false can print")