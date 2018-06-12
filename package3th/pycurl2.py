#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/12 14:22.

import pycurl
import certifi

with open('baidu.html', 'wb') as f:
    head = ['Accept:*/*', 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0)'
                          ' Gecko/20100101 Firefox/32.0']

    c = pycurl.Curl()
    c.setopt(c.URL, 'https://www.baidu.com/')
    c.setopt(c.HTTPHEADER, head)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()