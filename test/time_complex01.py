#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/29 17:43.

def use_t(n):
    for i in range(n):
        print('走路中...')
        print('走了一米')

def use_t1(n):
    i = 0
    while i < n:
        print('走路中...')
        print('走了一米')
        i += 1


# use_t(10)
use_t1(10)