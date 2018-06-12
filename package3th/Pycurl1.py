#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/12 10:57.

import pycurl
import certifi
from io import BytesIO




url = "https://www.baidu.com/"
head = ['Accept:*/*','User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0)'
                     ' Gecko/20100101 Firefox/32.0']

buff = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.HTTPHEADER,  head)
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.WRITEDATA, buff)
c.perform()
c.close()

print(buff.getvalue().decode())