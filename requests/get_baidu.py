#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/11 17:12.

import requests

r = requests.get('https://www.baidu.com/')
print(r)
print(r.status_code)
print(r.encoding)
print(r.text)
print(r.content)