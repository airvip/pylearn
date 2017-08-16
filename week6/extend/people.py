#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/16 11:32.

#经典类
#class People:
#新式类
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating"%self.name)

    def talk(self):
        print("%s is talking"%self.name)

    def sleep(self):
        print("%s is sleeping"%self.name)


class Relation(object):

    def make_friends(self,obj):
        print("%s is making frends with %s" %(self.name,obj.name))
        self.friends.append(obj)



class Man(People,Relation):

    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)#新式类写法
        self.money = money
        print("%s borning has %s money"%(self.name,self.money))

    def piao(self):
        print("%s is piaoing ...20s... done" %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Women(People,Relation):

    def get_birth(self):
        print("%s is born a baby..."%self.name)


man1 = Man("airvip",22,555)
man1.eat()
man1.piao()
man1.sleep()

women1 = Women("yaya",21)
women1.get_birth()


man1.make_friends(women1)

women1.name = "yueer"
print(man1.friends[0].name)