#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/9/18 15:29.

import os
import sys
import math
import requests
import urllib3
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

def save_img(img_url, file_name, file_path = './img/'):

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    all_path = file_path + file_name
    if os.path.exists(all_path):
        print('{}文件已经存在，跳过'.format(all_path))
    else:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
            }
            urllib3.disable_warnings()
            with requests.get(img_url, timeout=3, verify=False, headers=headers, stream=True) as response:
                total_size = int(response.headers['content-length'])
                size = 0 # 已保存资源大小
                chunk_size = 1024 # 每次保存资源大小
                print('[ %s 文件大小]：%.2f MB' % (file_name,(total_size / chunk_size / 1024)), end='')
                with open(all_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size):
                        if chunk:
                            file.write(chunk)
                            size += len(chunk)
                            print('\r'+'[下载进度]：%s %.2f %%' %('>'*int(size*50/total_size), float(size/total_size*100)), end='')
            print()
            return True
        except Exception as e:
            print('--{}保存失败--{}--'.format(all_path, e))
            return False

def name_processor(file_path):
    h5 = hashlib.md5()
    h5.update(file_path.encode('utf-8'))
    # 获得后缀
    file_suffix = os.path.splitext(file_path)[-1]
    name = h5.hexdigest() + '.' + file_suffix
    return name

if __name__ == '__main__':
    save_img('https://p3a.pstatp.com/weili/l/189459245242253771.jpg', './scense.jpg')