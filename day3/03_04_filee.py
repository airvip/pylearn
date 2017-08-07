#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/7 15:55.

import shutil

#shutil.copy("03_04_file","03_04_file.swp")

f = open("03_04_file","r",encoding="utf-8")
f_new = open("03_04_file.swp","w",encoding="utf-8")

for line in f:
    if "女人" in line:
        line = line.replace("女人","美女")
    f_new.write(line)

f.close()
f_new.close()