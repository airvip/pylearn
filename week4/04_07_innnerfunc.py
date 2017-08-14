#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 11:19.

'''
#全真为真
print(all([1,-2,3]))
print(all([0,-2,3]))
#一真为真
print(any([0,-2,3]))
print(any([]))

res = ascii([1,2,"ads"])
print(type(res),[res])

print(bin(3))
print(bin(5))

print(bool(1))
print(bool(0))

a = bytes("abc",encoding="utf-8")
print(a.capitalize(),a)

b = bytearray("abc",encoding="utf-8")
print(b[0])
b[1] = 100
print(b)

def sayhi():pass
print(callable(sayhi))

print(chr(97))
print(chr(98))

print(ord('a'))
print(ord('b'))

code = "for i in range(10):print(i)"
py_obj = compile(code,"","exec")
exec (py_obj)
exec(code)

d = dict()
print(d)
print(dir(d))

print(divmod(5,1))
print(divmod(5,3))

x = '1+1'
print(eval(x))

def say(n):
    print(n)
say(3)

(lambda n:print(n))(5)
calc = lambda n:print(n)
calc(50)

#filter 做筛选
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i,end=' ')
print(type(res))
#map 做操作
res = map(lambda n:n*n,range(10))
for i in res:
    print(i,end=' ')
print(type(res))


res = [n*n for n in range(10)]
for i in res:
    print(i,end=' ')
print(type(res))

import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)

print(hex(55))
print(hex(54))
'''
print(globals())
print(globals().get('local_var'))

print(oct(16))
print(oct(15))

print(pow(2,3))
print(pow(3,3))

print(round(1.2345,2))
print(round(13.2345,0))

d = {'name':'airvip','age':'13','3':'4','sd':'23','ad':'45','34':'55'}
print(sorted(d))
print(sorted(d.items()))
print(sorted(d.items(),key=lambda x:x[1]))
print(d)

a = [1,2,3,4]
b = ['a','b','c','d']
for i in zip(a,b):
    print(i)

__import__('04_01_decorator1')
