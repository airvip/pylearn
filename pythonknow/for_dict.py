#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/1/19 1:23.


'''
#最原始的迭代
dict = {"name":"airvip","age":24,"addr":"china"}
for i in dict:
    print("%s:%s" %(i,dict[i]))

#只对key进行迭代
for k in dict.keys():
    print(k)

for v in dict.values():
    print(v)

for (k,v) in dict.items():
    print(k,':',v)
'''

dict = {"name":"airvip","age":24,"addr":"china"}

i = iter(dict)
try:
    while True :
        print(next(i))
except:
    pass


