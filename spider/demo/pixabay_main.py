#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
from utils import save_img,  img_name_processor


def pixabay(keyword):
    img_cnt = 0
    folder, key = keyword, keyword
    if not folder: sys.exit('程序退出：未输入分类名称！')
    if not key: sys.exit('程序退出：未输入关键字！')

    query_url = 'https://pixabay.com/zh/photos/?q={}&image_type=photo'.format(key)
    query_res = requests.get(query_url)
    query_soup = BeautifulSoup(query_res.text, 'lxml')
    pic_num = query_soup.h1.text  # str
    print('-----共{}-----'.format(pic_num))
    page_num = query_soup.select('.add_search_params')[0].text.strip().lstrip('/ ')
    print('-----共{}页-----'.format(page_num))
    if "抱歉，我们没找到相关信息。" in query_res.text:
        return "抱歉，我们没找到相关信息。"
    for page in tqdm(range(1, int(page_num) + 1)):
        url = 'https://pixabay.com/zh/photos/?q={}&pagi={}'.format(key, page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        items = soup.select('.credits .item')
        # print(items)
        for item in items:
            img_attrs = item.a.img.attrs
            if img_attrs['src'] == '/static/img/blank.gif':
                img_src = img_attrs['data-lazy']
            else:
                img_src = img_attrs['src']
            path = r'D://人脸相关的图片//pixabay//{}'.format(keyword)
            if not os.path.exists(path):
                os.makedirs(path)
            filename = img_name_processor(img_src)
            file = os.path.join(path, filename)
            rt = save_img(file=file, src=img_src) # 是save_img的返回值，
            img_cnt += 1
            if img_cnt == pic_num:
                print("已搜集{}张{}图片，程序退出...".format(img_cnt, key))
                break
            if rt:
                print('第{}张[{}]图片保存成功...'.format(img_cnt, key))
            else:
                print('第{}张[{}]图片保存失败...'.format(img_cnt, key))


if __name__ == "__main__":
    # 女性 脸，美女，
    pixabay('美女')
