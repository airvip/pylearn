#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_divide(x, y):
    try:
        res = x / y
    except ValueError:
        print('error: value error')
    except (ZeroDivisionError, TypeError):
        print('error: params error')
    else:
        print('执行没有问题,结果为:%s' % res)
    finally:
        print('我就是用来做扫尾工作的')

my_divide(4,2) # 调用