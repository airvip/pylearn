#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        print('error: division by zero!')
    except TypeError:
        print('error: Type error')
    except ImportError:
        print('error: Import error')

my_divide(4,'4') # 调用