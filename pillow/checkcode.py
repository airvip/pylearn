#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/5/10 17:08.

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 获取随机字符
def get_char():
    t = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','g','k','m','n','p','q','r','s','t','u','v','w','x','y','z')
    return t[random.randint(0,len(t)-1)]

# 随机背景色
def rand_bg():
    return (random.randint(100,255), random.randint(100,255), random.randint(100,255))

# 随机文本色
def rand_col():
    return (random.randint(10, 80), random.randint(10, 80), random.randint(10, 80))

height = 40
font_num = 4
img = Image.new('RGB', (height * font_num, height), (255,255,255)) # 创建白底图片
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size=24) # 创建字体对象
draw = ImageDraw.Draw(img) # 创建画布实例
# 填充像素
for w in range(height * font_num):
    for h in range(height):
        draw.point((w,h), fill=rand_bg())

# 输出干扰线及文字
for t in range(font_num):
    # 参数一：起点坐标 [0,0] 或 （0,0）参数二：终点坐标 [0,0] 或 （0,0）参数三：填充颜色
    draw.line(((random.randint(0, height), random.randint(0, height)),(random.randint( height * (font_num - 1), height * font_num), random.randint(0, height))), fill=rand_col())
    # 参数一：坐标 [0,0] 或 （0,0） 参数二：字符 参数三：字体对象 参数四：填充颜色
    draw.text((height * t + 8, 8), get_char(), font=font, fill=rand_col())

img.save('code.jpg')

