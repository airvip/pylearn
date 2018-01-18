#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/18 17:41.

import os
import re
import json
import base64

path = 'F:/log/15_system.log'

fr = open(path,"r",encoding="utf-8")
fw = open("err.log","w",encoding="utf-8")


try:
    n = 0
    str = ''
    for line in fr:

        if re.search("开始调用云南省第二人民医院\(红会医院\)his接口", line):
            str = line
            n = 1

        if re.search("调用红会医院接口出现异常:Error Fetching http headers",line):
            str = line
            n = 2

        if (n == 1 and line.strip() == '') or (n == 2 and line.strip() == ''):
            fw.write('---------------------------------------------------------------\n')
            fw.write(str)
            if n == 1:
                print(re.search("{.*}",str).group())
                json.dump(re.search("{.*}",str).group(),fw)
                fw.write('\n')
                # fw.write(re.search("{.+",str))
            n = 0

finally:
    fr.close()

fw.close()