#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename my_err.py

class MyTypeError(TypeError):
    pass

def int_add(x,y):
    if not isinstance(x, int):
        raise MyTypeError('类型错误: %s' %x)
    if not isinstance(y,int):
        raise MyTypeError('类型错误: %s' %y)
    return x + y

int_add(2, 's')