#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        print('error: division by zero!')

my_divide(4,0) # 调用