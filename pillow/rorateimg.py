#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/10 14:50.

from PIL import Image, ImageFilter

img = Image.open('hzw.jpg')
w, h = img.size # 获取图片尺寸
print("图片尺寸 > 宽:%s 高：%s " %(w, h))
img.thumbnail((w//2, h//2)) # 等比例缩放到一半的尺寸
img2 = img.rotate(-45) # 顺时针旋转45度
img2 = img2.filter(ImageFilter.EMBOSS) # 增加浮雕
img2.save('newhzw.jpg')
n_w, n_h = img2.size # 获取图片尺寸
print("新图片尺寸 > 宽:%s 高：%s " %(n_w, n_h))