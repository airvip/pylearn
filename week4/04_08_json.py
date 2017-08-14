#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 17:05.

import json

info = {
    'name':'airvip',
    'age':22
}
f = open("json","w")
# f.write(str(info))
#print(json.dumps(info))
json.dump(info,f)#f.write(json.dumps(info))

f.close()
