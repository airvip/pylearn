#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/11 18:24.


import module_air as air
#import module1,module2
#from module_air import *#不推荐使用
#from module_air import log#不推荐使用
#from module_air import log,sayhi#不推荐使用

print(air.name)
air.sayhi()

def log():
    print("in the main")

air.log()