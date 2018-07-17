#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_divide(x, y):
    try:
        res = x / y
    except (ZeroDivisionError, TypeError):
        print('error: params error')
    else:
        print('执行没有问题,结果为:%s' % res)

my_divide(4,2) # 调用