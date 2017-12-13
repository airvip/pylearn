#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/16 16:47.

#Python2经典类(继承深度优先继承搜索法) 新式类（继承广度优先继承搜索法）
#Python3继承广度优先继承搜索法
class A(object):
    def __init__(self):
        print('A')

class B(A):
    # pass
    def __init__(self):
        print('B')

class C(A):
    pass
    def __init__(self):
        print('C')

class D(B,C):
    pass
D()

class E(C,B):
    pass
E()