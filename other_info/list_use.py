#!/usr/bin/env python3
# -*- coding:utf-8 -*-

list1 = ['00:00', '01:00', '02:00', '03:00', '04:00']

for i in  list1:
    print(i, end=' ')

print()

for i in range(len(list1)):
    print(i, end=' ')

print()

for i in enumerate(list1):
    print(i)


'''

for i, v in enumerate(list1):
    print(i,'=>',v)

for i, v in enumerate(list1, 1):
    print(i, '=>', v)

'''