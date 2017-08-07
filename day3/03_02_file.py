#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/7 9:38.

#data = open("03_02_file",encoding="utf-8").read()
'''
#file open only read
f = open("03_02_file_0","r",encoding="utf-8")
data = f.read()
f.close()
print(data)

#file only write
f = open("03_02_file_1","w",encoding="utf-8")
f.write("我爱北京天安门\n")
f.write("天安门上太阳升\n")
f.close()

#file append only write
f = open("03_02_file_1","a",encoding="utf-8")
f.write("when i was young i listen to the radio\n")
f.write("天安门上太阳升\n")
f.close()

f = open("03_02_file_0","r",encoding="utf-8")
for i in range(5):
    print(f.readline().strip())
f.close()
'''

f = open("03_02_file_0","r",encoding="utf-8")
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("line".center(50,"*"))
        continue
    print(line.strip())

f.close()