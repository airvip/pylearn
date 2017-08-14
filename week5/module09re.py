#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 17:46.

import re
#^在match没有作用
res = re.match("^air","airviplasy")
print(res)
print(res.group())

res = re.match("^airvip\d+","airvip123lasy123")
print(res.group())


res = re.match("^.+","airvip123lasy123")
print(res.group())
res = re.match("^.","airvip123lasy123")
print(res.group())


res = re.search(".\d","airvip123lasy123")
print(res.group())

res = re.search(".\d+$","airvip123lasy123")
print(res.group())

res = re.search("\d[a-z]+\d+$","airvip123lasy123")
print(res.group())


res = re.search("#.+#","airvip#123#lasy123")
print(res.group())
