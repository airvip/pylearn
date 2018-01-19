#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/18 17:41.

import os
import re
import json
import base64

path = 'F:/log/12_system.log'

fr = open(path,"r",encoding="utf-8")
fw = open("err12.log","w",encoding="utf-8")

try:
    n = 0
    strC = ''
    lineNo = 1
    set1 = set()
    for line in fr:

        if re.search("开始调用云南省第二人民医院\(红会医院\)his接口", line):
            strC = line
            n = 1
            continue

        # if re.search("调用红会医院接口出现异常:Error Fetching http headers",line):
        #     strC = line
        #     n = 2

        if n == 1 and line.strip() == '':
            fw.write(str(lineNo)+'----------------\n')
            lineNo += 1

            #将json格式化
            jsonStr = re.search("{.*}",strC).group()
            zhJson = json.loads(jsonStr)
            strC = ''
            for (key,val) in zhJson.items():
                if key == 'MobileNo':
                    set1.add(val)
                strC += "'{}':'{}'".format(key,val)
            strC += '\n'
            fw.write(strC)

        n = 0


    setStr = ''
    # n = 1
    for i in set1:
        setStr += '\''+i+'\','
        # if n >= 10:
        #     setStr += '\n'
        #     n = 0
        # n += 1
    fw.write(setStr)
finally:
    fr.close()
    fw.close()