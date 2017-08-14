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

res = re.search("[0-9]{3}","a2b1c234sd")
print(res.group())

res = re.findall("[0-9]{1,3}","a2b1c234sd")
print(res)

res = re.search("abc|ABC","ABCabcCD")
print(res.group())