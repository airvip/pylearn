#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import airutils

def getxiaohuapic():
    img_cnt = 0
    query_url = 'http://www.xiaohuar.com/hua/'
    query_res = requests.get(query_url)
    query_soup = BeautifulSoup(query_res.text, 'lxml')
    img_num = query_soup.select("a[title='总数'] b")[0].get_text()
    print("----总共有{}张的图片----".format(img_num))
    page_dom = query_soup.select('.page_num a')
    page_num = re.search("(\d)-(\d+)", page_dom[len(page_dom)-1].attrs['href']).group(2)
    print("----总共有{}页的图片----".format(page_num))
    for page in range(1, int(page_num) + 1):
        url = 'http://www.xiaohuar.com/list-1-{}.html'.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        items = soup.select('.item_t .img')
        for item in items:
            img_attrs = item.a.img.attrs
            img_src = 'http://www.xiaohuar.com'+img_attrs['src']
            filename = airutils.name_processor(img_src)
            path = 'D:/spider/xiaohua'
            res = airutils.save_img(img_url=img_src, file_name=filename, file_path=path)
            img_cnt += 1
            if res:
                print('第{}张图片{}保存成功...'.format(img_cnt, filename))
            else:
                print('第{}张图片{}保存失败...'.format(img_cnt, filename))


if __name__ == "__main__":
    getxiaohuapic()

