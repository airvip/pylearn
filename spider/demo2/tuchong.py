# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:20

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import airutils
import re



def tuchongfree(keyword: str, pages=3):
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
            src = item.get_attribute('style')
            if not src:
                continue
            img_src = 'https://' + re.search('"//(.*)\.webp"',src).group(1) + '.jpg'
            filename = airutils.name_processor(img_src)
            path = 'D:/tuchong_com/{}'.format(keyword)
            res = airutils.save_img(img_url=img_src, file_name=filename, file_path=path)
            img_cnt += 1
            if res:
                print('第{}张图片{}保存成功...'.format(img_cnt, filename))
            else:
                print('第{}张图片{}保存失败...'.format(img_cnt, filename))


    driver.close()

if __name__ == "__main__":
    tuchongfree(keyword='女孩', pages=1)
