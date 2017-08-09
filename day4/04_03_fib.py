#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 23:52.

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print(b,end=" ")
        yield b
        a,b=b,a+b
        n +=1
    return 'over'

g = fib(10)
print(g)

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
