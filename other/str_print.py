#!/usr/bin/env python3
# -*- coding:utf-8 -*-


print("我是%s" %'air')

# r 原格式输出
print("我是%r" %'air')

# c 使用字符直接显示
print("性别%c。" % 'Y')

# - 居左 | width 宽度  |  c 使用数字转字符 
print("性别%-10c。" %89)

# o 转八进制
print("今年%o" % 24)

# x 转十六进制
print("今年%x" % 24)

# d 整数显示
print("今年%d" % 24.34)

# 综合使用
print("我是%s，今年%5d，性别%-10c。" %('air', -24, 'Y'))  

# 0 填充
print("我是%s，今年%05d。" %('air', -24))

# 0 填充
print("我是%s，今年%05d。" %('air', 24))

# f 浮点数
print("我是%s，薪资%.3f元" %('air', 23444432.35656))

# e 科学技术法 
print("我是%s，薪资%.3e元" %('air', 23444432.5435))

# E 科学计数法
print("我是%s，薪资%.3E元" %('air', 23444432.5435))

# g G 自动转换
print("我是%s，今天收入%g，花费%G。" %('air', 1000000, 100))

# (name) 使用
print("我是%(name)s，今年%(age)5d，性别%(sex)-10c。" %{'name':'air', 'age':24, 'sex':'Y'})

# % 使用
print("我是%s, 100%%的时间在学习。" %'air')
