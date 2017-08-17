#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 15:25.

class Dog(object):

    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food[%s]"%food)
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("delete over")

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)


d = Dog("larui")
d(1,2,3,lay="airvip")

Dog("mm")(1,2,3,lay="airvip")

d.eat
d.eat = "baozi"
d.eat

del d.eat
