#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class PeopleMetaclass(type):
        def __new__(cls, name, bases, attrs):
            attrs['default_name'] = 'airvip'
            attrs['setname'] = lambda self:print(dir(self))
            print(cls)
            print(name)
            print(bases)
            print(attrs)
            # return type.__new__(cls, name, bases, attrs)
            return super(PeopleMetaclass, cls).__new__(cls, name, bases, attrs)

class MyPeople(object,metaclass=PeopleMetaclass):
    # __metaclass__ = PeopleMetaclass
    pass

print(MyPeople.default_name)
print(MyPeople.setname)
MyPeople.setname(MyPeople)
print(dir(MyPeople))

