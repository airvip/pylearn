#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 17:46.

import re

'''
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

res = re.search("\A[0-9]{2,4}[a-z]\Z","23d")
print(res,1)

res = re.search("^\D{3}"," \r\n adsf")
print(res)

res = re.search("(abc){2}","23abcabc|airvip")
print(res)

res = re.search("(abc){2}\|","23abcabc|airvip")
print(res)

res = re.search("\w{2,3}","a irvipsd123")
print(res)

res = re.search("\W{2,3}","a \rvipsd123")
print(res)

res = re.search("\s+","\r    \n")
print(res)


res = re.search("(?P<id>[0-9]+)","sbc1234ds")
print(res)
res = re.search("(?P<id>[0-9]{4})","sbc1234ds").group()
print(res)
res = re.search("(?P<id>[0-9]{4})","sbc1234ds").group("id")
print(res)
res = re.search("(?P<id>[0-9]{4})(?P<name>\w+)","sbc1234airvip").groupdict()
print(res)

res = re.search("(?P<province>\d{4})(?P<city>\d{2})(?P<birthday>\d{8})","371425199609092011").groupdict()
print(res)

res = re.split("[0-9]+","ab23sd32b45ds")
print(res)

res = re.sub("[0-9]+","**","ab23sd32b45ds",count=0)
print(res)
'''


res = re.search(r"\\","abc\\12dsfH")
print(res)

res = re.search(r"\\",r"abc\12")
print(res)

res = re.search("[a-z]{3}","2sAsi",flags=re.I)
print(res)


res = re.search("[a-z]+s$","addd\nfdasds\r\nsdfsds")
print(res)
res = re.search("[a-z]+s$","addd\nfdasds\r\nsdfsds",flags=re.M)
print(res)