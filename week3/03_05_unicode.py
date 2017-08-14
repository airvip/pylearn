#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/7 16:46.

import sys
print(sys.getdefaultencoding())

s = u"你好"
print(s)
unicode_to_gbk = s.encode("gbk")
print(unicode_to_gbk)


gbk_to_unicode = unicode_to_gbk.decode("gbk")
print(gbk_to_unicode)


