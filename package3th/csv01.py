#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tablib

data = tablib.Dataset()
data.headers = ('序号', '姓名', '年龄', '分值')

datalist = [
    [1, '张三', 25, 18],
    [2, '李四', 24, 99],
    [3, '王五', 16, 90]
]

for val in datalist:
    data.append(val)

data.append([4, '木子', 18, 100])
data.insert(0, [0, '维奇', 23, 100])
print(data)

# 导出 xls
# with open('dataxls.xls', 'wb') as f:
#     f.write(data.xls)