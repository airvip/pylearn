#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 15:17.

import xml.etree.ElementTree as ET

tree = ET.parse("xmllearn.xml")
#print(tree)
root = tree.getroot()
# print(root.tag)
# print(root)

#遍历xml文档
for child in root:
    if child.tag == 'data':
        print('data'.center(20,"*"))
        for i in child:
            print('tagname='+i.tag,'content='+i.text,'attrib='+str(i.attrib))
    else:
        print('tagname='+child.tag,'content='+child.text)
