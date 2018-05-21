#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/9 15:37.

# 整个区块显示：高亮红色
print("\033[1;31m")
print("*"*20)
print("姓名：阿尔维奇")
print("住址：中国")
print("年龄：24 岁")
print("*"*20)
print("\033[0m")

# 下划线 字体:白色
print("\033[4;37m长得这么漂亮一定是蓝孩子\033[0m")

# 绿色字反显 即 背景色与字体色调换
print("\033[7;32m我要小姐姐\033[0m")