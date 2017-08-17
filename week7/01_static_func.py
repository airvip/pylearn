#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 9:42.

class Dog(object):
    name = "chu"

    def __init__(self,name):
        self.name = name

    # def eat(self,food):
    #     print("%s is eating %s" %(self.name,food))

    @staticmethod#实际上根类没什么关系
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

    @classmethod
    def walk(self):
        print("%s is walking with girlfriend"%self.name)

    def talk(self):
        print("%s is talking" %(self.name))

d = Dog('mary')
d.eat(d,"root")
d.talk()
d.walk()