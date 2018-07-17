#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_divide(x, y):
    try:
        try:
            res = x / y
            return res
        except NameError:
            print('error: Name error')
        except ImportError:
            print('error: Import error')
    except :
        print('error: error undefined')

my_divide(4,'4')