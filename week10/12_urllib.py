#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/4 23:09.

from urllib import request
import time
import gevent
from gevent import monkey

monkey.patch_all()#将当前程序的所有的io操作给我单独做上标记

def f(url):
    print("GET:%s"%url)
    resp = request.urlopen(url)
    data = resp.read()
    # f = open("url.html","wb")
    # f.write(data)
    # f.close()
    print("%d bytes received from %s."%(len(data),url))

# f("http://cn.ynhdkc.com/admin/index/index")

url = [
    "http://www.dear521.com/",
    "http://www.dear521.com/home/blog/index/id/70.html",
    "http://www.dear521.com/home/blog/index/id/20.html"
]
sync_time_start = time.time()
for i in url:
    f(i)
print("sync cost",time.time()-sync_time_start)


async_start_time = time.time()
gevent.joinall([
    gevent.spawn(f,"http://www.dear521.com/"),
    gevent.spawn(f,"http://www.dear521.com/home/blog/index/id/70.html"),
    gevent.spawn(f,"http://www.dear521.com/home/blog/index/id/20.html")
])
print("async cost:",time.time() - async_start_time )
