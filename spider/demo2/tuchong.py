# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:20

import time

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import airutils



def tuchongfree(keyword: str, pages=10):
    """本函数用于爬共享图库"""
    img_cnt = 0
    driver=webdriver.Chrome()
    driver.maximize_window()
    url = 'https://stock.tuchong.com/free/search/?term={}'.format(keyword)
    driver.get(url)
    # driver.find_element_by_class_name('search-input').click()
    for page in range(pages):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(random.randint(1, 4))
        items = driver.find_elements_by_class_name('img')
        for item in items:
            print(item)
            src = item.get_attribute('style')
            print(src)
            # if not src:
            #     continue
            # filename = airutils.name_processor(src)
            # path = 'D:/tuchong_com/{}'.format(keyword)
            # if not os.path.exists(path):
            #     os.makedirs(path)
            # file = os.path.join(path, filename)
            # res = airutils.save_img(file=file, src=src)
            # img_cnt += 1
            # if res:
            #     print('第{}图片保存成功...'.format(img_cnt))
            # else:
            #     print('第{}张图片保存失败...'.format(img_cnt))

    driver.close()

if __name__ == "__main__":
    # 女脸，女脸部，
    tuchongfree(keyword='风景', pages=10)
