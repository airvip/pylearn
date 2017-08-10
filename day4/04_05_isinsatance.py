#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 9:48.


#可迭代的 Iterable
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance("abc",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(123,Iterable))

print("line".center(20,"*"))

#迭代器 Iterator
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance("abc",Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(123,Iterator))

#转迭代器 iter
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter("abc"),Iterator))
print(isinstance(iter(123),Iterator))