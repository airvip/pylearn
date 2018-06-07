#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/7 10:27.

import chardet

b1 = '你好'.encode()
res = chardet.detect(b1)
print(res)


print(chardet.detect(b'hello 123'))


print(chardet.detect('你好 123'.encode('gbk')))