#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/18 10:26.

def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s"%(self.name,food))



d = Dog("yoyo")
choice = input(">>$").strip()

if hasattr(d,choice):
    attr = getattr(d,choice)
    # print(type(attr) == 'str')
    # print(isinstance(attr,str))
    if isinstance(attr,str):
        # setattr(d,choice,"haha")#改名
        delattr(d,choice)#删名
    else:
        attr('meat')
else:
    # setattr(d,choice,bulk)
    # d.talk(d)
    setattr(d,choice,'22')
    print(getattr(d,choice))
# print(hasattr(d,choice))
# print(getattr(d,choice))

print(d.name)

'''
if choice == 'eat':
    d.eat()

'''
