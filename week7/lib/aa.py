#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 17:12.

class AA(object):

    def __call__(self, *args, **kwargs):
        print("call")

    def __init__(self):
        self.name = 'airvip'

AA()()