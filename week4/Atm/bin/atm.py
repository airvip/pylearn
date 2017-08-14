#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/10 18:43.

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print(BASE_DIR)
sys.path.append(BASE_DIR)
from  conf import setting
from  core import main

main.login()