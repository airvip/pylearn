#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/13 0:03.


import time
'''
# print(time.altzone())
print(time.asctime((2017,8,13,0,12,36,6,225,0)))
print(time.clock())
print(time.ctime())
print(time.gmtime(1234567890))
'''

print("line times str and time tuple".center(50,"*"))
#return time tuple
time_tuple = time.localtime()
print(time_tuple)
# time_tuple = (2017,8,13,0,12,36,6,225,0)
#time tuple 2 time str
time_str = time.asctime(time_tuple)
print(time_str)
time_str = time.strftime("%Y-%m-%d %H:%M:%S",time_tuple)
print(time_str)
#time str 2 time tuple
time_tuple = time.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(time_tuple)
print("line timestamp and time tuple".center(50,"*"))
#time tuple 2 timestamp
timestamp = time.mktime(time_tuple)
print(timestamp)
#timestamp 2 time tuple
time_tuple = time.localtime(timestamp)
print(time_tuple)
#return time timestamp
timestamp = time.time()
print(timestamp)
print("line timestamp and time str".center(50,"*"))
time_str = time.ctime(timestamp)
print(time_str)