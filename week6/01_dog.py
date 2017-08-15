#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/15 15:39.

class Dog:

    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s:wang wang wang" %self.name)

d1 = Dog('dog1')
d2 = Dog('dog2')
d3 = Dog('dog3')

d1.bulk()
d2.bulk()
d3.bulk()

