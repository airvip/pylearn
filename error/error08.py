#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename my_err.py

def my_divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        print('error: division by zero!')
    except:
        print('error: unexpected error')
        raise

my_divide(4,'4') # 调用