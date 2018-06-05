#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from PIL import Image

# You can add another str to change chars(left to right, black to white):
str1 = "@@WW##QQOOoo**--::''      "
str2 = "01. "
chars = list(str1)


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return chars[int(gray / 256.0 * len(chars))]


if __name__ == '__main__':
    im = Image.open('mz.png')
    w = int(im.size[0] / 4)
    h = int(im.size[1] / 4)
    im = im.resize((w, h), Image.ANTIALIAS)

    im = im.convert('RGBA')

    txt = ""
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            txt += get_char(*im.getpixel((i, j)))
        txt += '\n'

    with open("chars.txt", 'w') as f:
            f.write(txt)
