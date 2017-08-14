#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/6 23:30.


list_1 = [1,2,4,5,7,6,7]
list_1 = set(list_1)

print(list_1,type(list_1))

list_2 = set([2,6,33,23,44])
print(list_1,list_2)

#jiao cha
print(list_1.intersection(list_2))
#bing ji
print(list_1.union(list_2))
#cha ji
print(list_1.difference(list_2))
print(list_2.difference(list_1))

print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))

print(list_1.symmetric_difference(list_2))