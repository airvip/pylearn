#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 10:52.

it = iter([1,2,3,4,5,6])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

