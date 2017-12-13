#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/14 23:38.


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    from modules.actions import excute_from_command_line
    execute_from_command_line(sys.argv)

































