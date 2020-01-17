#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2019/12/14 13:25.
from pyquery import PyQuery as pq
import re



def duanziwang():
    with open("./dyt.html", "r", encoding="utf-8")as f:
        content = f.read()

    res = pq(content)
    articles = res.find('.weui_media_box')
    # for article in range(len(articles)):
    for article in articles:
        # print(pq(article))
        url_src = pq(article).find('span.weui_media_hd').attr('style')
        if url_src is None:
            continue
        url_res = url_src[21:-1]

        title = pq(article).find('h4').html()
        if pq(title).find('.icon_original_tag'):
            title = title.replace('<span id="copyright_logo" class="icon_original_tag">原创</span>', '')
        title = title.strip()

        time_str =  pq(article).find('.weui_media_extra_info').html()
        t = time_str.replace('<span id="copyright_logo" class="icon_original_tag">原创</span>','')

        ad = pq(article).find('h4').attr('hrefs').strip()
        # print(t+'\n'+title+'\n'+url_res+'\n'+ ad)
        print(t+'\n'+title+'\n'+ ad)







if __name__ == "__main__":
    duanziwang()