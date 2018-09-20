#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/9/18 15:29.

import os
import sys
import math
from urllib import request
import hashlib


def schedule(count, block_size, total_size):
    '''
    进度条
    count: 已经下载的数据块
    block_size: 数据库块的大小
    total_size: 远程文件的大小
    '''
    percent = 100 if int(count * block_size * 100 / total_size) > 100 else int(count * block_size * 100 / total_size)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.write('[%-50s] %s' % ('=' * int(math.floor(count * block_size * 50 / total_size)), percent))
    sys.stdout.flush()

def save_img(src, file = ''):
    if os.path.exists(file):
        print('{}文件已经存在，跳过'.format(file))
    else:
        try:
            request.urlretrieve(src, file, reporthook=schedule)
            return True
        except Exception as e:
            print('--{}保存失败--{}--'.format(file, e))


def name_processor(src):
    h5 = hashlib.md5()
    h5.update(src.encode('utf-8'))
    ext_split = src.split('.')
    name = h5.hexdigest() + '.' + ext_split[len(ext_split) - 1]
    return name

if __name__ == '__main__':
    save_img('http://www.xiaohuar.com/d/file/20170628/f3d06ef49965aedbe18286a2f221fd9f.jpg', './xiaohua.jpg')