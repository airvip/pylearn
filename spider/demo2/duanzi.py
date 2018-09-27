#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
import re


def duanziwang():
    url = 'http://duanziwang.com/page/{}'.format(1)
    res = pq(url)
    page_dom = res.find('.page-number').html()
    total_page = int(re.search('共 (.*) 页', page_dom).group(1))
    print(total_page)
    file_name = './duanzi.txt'
    for i in range(1,total_page+1):
        with open(file_name, 'a+', encoding='utf-8') as fw:
            fw.write('写入第 {} 页的段子\n'.format(i) + '*'*50 + '\n')
        query_url = 'http://duanziwang.com/page/{}'.format(i)
        query_res = pq(query_url)
        articles = query_res.find('.post')
        for article in range(len(articles)):
            title = query_res.find('.post-title a').eq(article).html()
            content = query_res.find('.post-content p').eq(article).html()
            if None == content:
                print('由于第 {} 页的第 {} 条段子没有内容跳过'.format(i, article + 1))
                continue
            if re.search('<img', content):
                print('由于第 {} 页的第 {} 条段子是图片跳过'.format(i, article + 1))
                continue
            content = content.replace('<br/>', '\n')
            str = '标题:' + title + '\n\n' + content + '\n' + '-'*50 + '\n'
            with open(file_name, 'a+', encoding='utf-8') as fw:
                fw.write(str)
            print('写入第 {} 页的第 {} 条段子'.format(i, article+1))



if __name__ == "__main__":
    duanziwang()