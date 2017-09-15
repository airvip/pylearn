#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/15 0:08.


def print_err(msg,quit=False):
    output = "\033[31;1mError:%s\033[0m"%msg
    if quit:
        exit(output)
    else:
        print(output)