#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/16 18:01.

class Animal:
    def __init__(self,name):
        self.name =name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        # return "Meow!"
        print("Meow!")

class Dog(Animal):
    def talk(self):
        # return "Woof! Woof!"
        print("Woof! Woof!")
'''
d = Dog("rourou")
d.talk()

c = Cat("sisi")
c.talk()
'''





c = Cat("sisi")
d = Dog("rourou")


# def animal_talk(self, obj):
#     obj.talk()

Animal.animal_talk(c)
Animal.animal_talk(d)
