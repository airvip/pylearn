#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/12 22:52.

import apackage

import sys,os


print(1,sys.path)
print(2,__file__)
print(3,os.path.basename(__file__))
print(4,os.path.abspath(__file__))
print(5,os.path.dirname(__file__))
print(6,os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__))+'\module_learn')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\module_learn')
import module_air

module_air.sayhi()

# print(os.path.basename(os.path))




