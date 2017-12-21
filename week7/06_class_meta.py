#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/17 23:37.

class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print("----MyType init ----")
        super(MyType, self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print("----Mytype call----")
        obj = self.__new__(self,*args,**kwargs)

        self.__init__(obj,*args,**kwargs)


class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo ----init----")

    def __new__(cls, *args, **kwargs):
        print("Foo --new--")
        return object.__new__(cls)



#第一阶段：解释器从上到下解释代码创建Foo类
#第二阶段：通过Foo类创建obj对象
obj = Foo("air")
