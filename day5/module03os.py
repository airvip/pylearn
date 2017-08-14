#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/13 0:46.

import os

print(os.getcwd())
print(os.chdir("E:\\workspace\pylearn\day5"))
print(os.chdir(r"E:\workspace\pylearn\day5"))

print(os.curdir)
print(os.pardir)
#递归创建目录,存在创建失败
#os.makedirs(r"E:\workspace\pylearn\day5\dir")
#os.removedirs(r"E:\workspace\pylearn\day5\dir")
#当前目录创建,存在创建失败
#os.mkdir("dir")
#os.rmdir("dir")

print(os.listdir('.'))
#删除文件
#os.remove()
#os.rename(oldname,newname)

print(os.stat(r"E:\workspace\pylearn\day5\01_package.py"))
#输出操作系统特定的路径分隔符,win下"\\",linux下"/"
print(os.sep)
#输出操作系统的行中止符,win下"\r\n",linux下"\n"
print(os.linesep)
#输出用于分割文件路径的字符串
print(os.pathsep)
#系统平台
print(os.name)
os.system("cls")
print(os.environ)

print(os.path.abspath(__file__))

print(os.path.split(__file__))
print(os.path.dirname(__file__))
print(os.path.basename(__file__))
print(os.path.exists(__file__))
print(os.path.isabs(__file__))
print(os.path.isfile(__file__))
print(os.path.isdir(__file__))

print(os.path.join(r"E:",r"a.txt"))
print(os.path.join(r"E:",r"\a",r"a.txt"))

print(os.path.getatime(__file__))
print(os.path.getmtime(__file__))
print(os.path.getctime(__file__))

