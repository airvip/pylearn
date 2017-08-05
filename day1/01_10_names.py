#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on  14:25.

names = "wzb airvip youyou nano"

names = ["wzb","airvip","youyou","nano"]
print(names)
print(names[0])
print(names[0:2])
print(names[:2])
print(names[-1])
print(names[-2:])
print(names[:-3:-1])
names.append("ata")
print(names)
names.insert(1,'lisa')
names.insert(1,['lili','yaka'])
print(names)
names[2] = 'xue'
print(names)
print(names.pop(3))
print(names)
names.remove('wzb')
print(names)
del names[2]
print(names)
print(names.index('xue'))
names.insert(3,'xue')
print(names.count('xue'))
# names.clear()
print(names)
names.reverse()
print(names)
names[-1] = 'lasa'
names.sort()
print(names)
names2 = [1,2,3,4]
names.extend(names2)
print(names)
#print(names2)
#del names2
#print(names2)
names.insert(4,[5,6])
#names2 = names.copy()
import copy
names2 = copy.deepcopy(names)
print(names2)
names[3] = "雪儿"
names[4][0] = "lala"
print(names)
print(names2)
print(names[::2])

for i in names:
    print(i)