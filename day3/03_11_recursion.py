#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 10:10.

def calc(n):
    print(n)
    tmp = int(n/2)
    if tmp > 0:
        return calc(tmp)
    print("->",n)
calc(10)