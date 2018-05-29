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

data.pop()
data.lpop()
del data[0:2]

data.append_col(['男'], header='性别')
data.insert_col(2, ['中国'], header='国籍')

del data['性别']



# print(data)

# print('JSON',data.export('json'))
# print('JSON',data.json)
# print('YAML',data.export('yaml'))
# print('YAML',data.yaml)
# print('CSV',data.export('csv'))
# print('CSV',data.csv)


# 导出 xls
with open('dataxls.xls', 'wb') as f:
    f.write(data.xls)
