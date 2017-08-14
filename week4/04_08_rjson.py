#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 17:16.

import json

f = open('json','r')
data = json.load(f)#data = json.loads(f.read())
f.close()


print(data["age"])
print(data)