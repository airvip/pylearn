#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import os
import hashlib
import urllib.request

def getxiaohua():
    img_cnt = 0
    query_url = 'http://www.xiaohuar.com/hua/'
    query_res = requests.get(query_url)
    query_soup = BeautifulSoup(query_res.text, 'lxml')
    img_num = query_soup.select("a[title='总数'] b")[0].get_text()
    print("----总共有{}张的图片----".format(img_num))
    page_dom = query_soup.select('.page_num a')
    page_num = re.search("(\d)-(\d+)", page_dom[len(page_dom)-1].attrs['href']).group(2)
    print("----总共有{}页的图片----".format(page_num))

    for page in tqdm(range(1, int(page_num) + 1)):
        url = 'http://www.xiaohuar.com/list-1-{}.html'.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        items = soup.select('.item_t .img')
        for item in items:
            img_attrs = item.a.img.attrs
            path = 'D:/xiaohuar_com/xiaohua'
            if not os.path.exists(path):
                os.makedirs(path)
            filename = img_name_processor(img_attrs['src'])
            file = os.path.join(path, filename)
            # 是save_img的返回值，
            # res = save_img(file=file, src='http://www.xiaohuar.com'+img_attrs['src'])
            if int(img_cnt) - 50 > int(img_num):
                print("已搜集{}张图片，程序退出...".format(img_cnt))
                break
            img_cnt += 1
            if os.path.exists(file):
                print('{}文件已经存在，跳过'.format(file))
            else:
                try:
                    urllib.request.urlretrieve('http://www.xiaohuar.com'+img_attrs['src'], file)
                    print('第{}张图片保存成功...'.format(img_cnt))
                except Exception as e:
                    print('--{}--'.format(e))
                    print('第{}张图片保存失败...'.format(img_cnt))


def img_name_processor(src):
    h5 = hashlib.md5()
    h5.update(src.encode('utf-8'))
    ext_split = src.split('.')
    img = h5.hexdigest() + '.' + ext_split[len(ext_split) - 1]
    return img


if '__main__' == __name__:
    getxiaohua()