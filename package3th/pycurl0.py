#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/12 14:01.

import pycurl
from io import BytesIO

url = "http://blog.diff.wang/"

buff = BytesIO()
c = pycurl.Curl() # 实例化
c.setopt(c.URL, url) # 设置请求地址
c.setopt(c.WRITEDATA, buff) # 写入请求的数据
c.perform() # 执行操作
c.close() # 关闭实例

print(buff.getvalue().decode()) # 打印请求的内容