#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 10:02.

name = ['yaya','airvip','coco']

def chang_name():
    name[0] = "丫丫"
    print("inner function",name)

chang_name()
print(name)