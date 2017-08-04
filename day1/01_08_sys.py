#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 16:02.

'''
import sys
#print(sys.path)
print(sys.argv)
print(sys.argv[2])
'''

import os
#linux
#os.system('dir')
#linux
#os.system('ls')

cmd_res = os.popen('ls')
print(cmd_res.read())

os.mkdir("new_dir")