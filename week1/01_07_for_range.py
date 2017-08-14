#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 13:59.

for i in range(0,10):
    if i<5:
        continue
    else:
        print('loop',i)


for i in range(10):
    print('--------',i)
    for v in range(10):
        if v > 5:
            break
        print(v)