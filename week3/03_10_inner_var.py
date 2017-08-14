#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 9:42.



'''
school = "12306"

def change_name(name):
    global school
    school = "17951"
    print(name)
    name = "AIR VIP"
    print(name)

name = "airvip"
change_name(name)
print(name)
print(school)
'''


#下面代码谁用开除谁

def change_variable():
    global lala
    lala = "17951"

change_variable()
print(lala)