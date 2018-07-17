#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/9 13:49.


from PIL import Image

img = Image.open('hzw.jpg')
img.show()
print(img.info)
print(img.size)
print(img.mode)
print(img.format)
