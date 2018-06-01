#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/1 17:02.

from xpinyin import Pinyin
import sys

p = Pinyin()

name = p.get_pinyin("阿尔维奇")

print(name)


print(u"你好")

print(sys.getdefaultencoding())
print(isinstance("你好", str))

