# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:20

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import airutils
import re



def tuchongfree():
    for i in range(863,943):

        if i < 10:
            i = '00'+str(i+1)
        elif i < 100:
            i = '0' + str(i+1)
        else:
            i = str(i+1)

        img_src = 'http://q3.pdfdo.com/Download/121316523714{}.jpg'.format(i)
        filename = '121316523714{}.jpg'.format(i)
        path = 'D:/1130'
        res = airutils.save_img(img_url=img_src, file_name=filename, file_path=path)
        if res:
            print('第{}张图片{}保存成功...'.format(i, filename))
        else:
            print('第{}张图片{}保存失败...'.format(i, filename))



if __name__ == "__main__":
    tuchongfree()
    # print(list(range(863,943)))