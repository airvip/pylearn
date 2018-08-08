#!/usr/bin/env python3
# -*- coding:utf-8 -*-



print("我是{},今年{}".format('air', 24))

print("我是{0},今年{1},我是{0}".format('air', 24))


print("我是{0[0]},今年{0[1]}".format(['air', 24]))


print("我是{name},今年{age}".format(name='air', age=24))


print("我是{name},今年{age}".format(**{'name':'air', 'age':24}))


print("我是{},今天收入{:20,.2%}".format('air', 24542353.2543))


print("我是{},今天收入{:20,.2f}".format('air', 24542353.2543))


print("我是{},今天收入{:20,.2e}".format('air', 24542353.2543))

print("我是{},今天收入{:20,.2e}".format('air', 24542353))
