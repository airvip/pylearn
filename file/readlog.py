#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/18 17:41.

import os
import re
import json
import base64

path = 'F:/log/18_system.log'

fr = open(path,"r",encoding="utf-8")
fw = open("err18.log","w",encoding="utf-8")


try:
    n = 0
    strC = ''
    lineNo = 1
    for line in fr:

        if re.search("开始调用云南省第二人民医院\(红会医院\)his接口", line):
            strC = line
            n = 1

        if re.search("调用红会医院接口出现异常:Error Fetching http headers",line):
            strC = line
            n = 2

        if (n == 1 and line.strip() == '') or (n == 2 and line.strip() == ''):
            fw.write(str(lineNo)+'----------------\n')
            lineNo += 1
            #记录时间
            matchStr = re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", strC)
            if matchStr:
                timeStr = re.sub('T',' ',matchStr.group())
                fw.write(timeStr + '\n')

            #将json格式化
            if n == 1:
                jsonStr = re.search("{.*}",strC).group()
                zhJson = json.loads(jsonStr)
                strC = ''
                for (key,val) in zhJson.items():
                    strC += "'{}':'{}'".format(key,val)
                strC += '\n'
            fw.write(strC)
            n = 0
finally:
    fr.close()
    fw.close()