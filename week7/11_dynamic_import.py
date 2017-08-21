#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/21 15:04.

import importlib
lib = importlib.import_module("lib.aa")
print(lib.AA().name)


lib = __import__("lib.aa")
obj = lib.aa.AA()
print(obj.name)

'''
print(mod)
instance = getattr(mod.aa,'AA')

obj = instance()
print(obj.name)
'''