#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/18 11:47.

class SelfExcept(Exception):
    def __init__(self,msg):
        self.message = msg

    # def __str__(self):
    #     return self.message


try:
    raise SelfExcept("you are bad")
except SelfExcept as e:
    print(e)