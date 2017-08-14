#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 11:16.

import shutil,os,sys

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

'''
shutil.copy(r"01_package.py",r"01_package_copy.py")# == copyfile + copymode


shutil.copyfile(r"01_package.py",r"01_package_copy.py")
#只copy源文件的权限，没有目标文件会报错
shutil.copymode(r"01_package.py",r"01_package_copy.py")

f1 = open(r"01_package.py",'r',encoding="utf-8")
f2 = open(r"01_package_copy1.py","w",encoding="utf-8")
 shutil.copyfileobj(f1,f2)

 shutil.copytree("apackage","apackage_copy")
 shutil.rmtree("apackage_copy")

 shutil.make_archive("apackage_zip","zip",root_dir=r"E:\workspace\pylearn\day5\apackage")
'''








