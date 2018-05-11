#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/11 17:56.

import requests

# r = requests.get('https://github.com/search?q=requests')
# print(r.status_code)
# print(r.text)


r = requests.get('https://github.com/search',params={'q':'requests'})
print(r.status_code)
print(r.text)