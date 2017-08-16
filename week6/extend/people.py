#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/16 11:32.

class People:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating"%self.name)

    def talk(self):
        print("%s is talking"%self.name)

    def sleep(self):
        print("%s is sleeping"%self.name)

class Man(People):

    def piao(self):
        print("%s is piaoing ...20s... done" %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Women(People):

    def get_birth(self):
        print("%s is born a baby..."%self.name)

man1 = Man("airvip",22)
man1.eat()
man1.piao()
man1.sleep()

women1 = Women("yaya",21)
women1.get_birth()