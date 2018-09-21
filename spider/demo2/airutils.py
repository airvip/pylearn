#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/9/18 15:29.

import os
import sys
import math
import requests
from urllib import request
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

    all_path = os.path.join(file_path, file_name)
    if os.path.exists(all_path):
        print('{}文件已经存在，跳过'.format(all_path))
    else:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
            }
            urllib3.disable_warnings()
            with requests.get(img_url, timeout=10, verify=False, headers=headers, stream=True) as response:
                if 'content-length' in response.headers.keys():
                # request.urlretrieve(img_url, all_path, reporthook=schedule)
                    total_size = int(response.headers['content-length'])
                    size = 0 # 已保存资源大小
                    chunk_size = 1024 # 每次保存资源大小
                    print('[文件大小]：%.2f MB' % ((total_size / chunk_size / 1024)), end='')
                    with open(all_path, 'wb') as file:
                        for chunk in response.iter_content(chunk_size):
                            if chunk:
                                file.write(chunk)
                                size += len(chunk)
                                print('\r'+'[下载进度]：%s %.2f %%' %('>'*int(size*50/total_size), float(size/total_size*100)), end='')
                elif 'transfer-encoding' in response.headers.keys() and 'chunked' == response.headers['transfer-encoding']:
                    # request.urlretrieve(img_url, all_path, reporthook=schedule)
                    with open(all_path, 'wb') as file:
                        print('[下载进度]：', end='')
                        for chunk in response.iter_content(1024):
                            if chunk:
                                file.write(chunk)
                                sys.stdout.write('>')
                                sys.stdout.flush()
                        else:
                            sys.stdout.write(' 100.00 %')
                            sys.stdout.flush()
                else:
                    return False
                print()
                return True
        except Exception as e:
            print(img_url)
            print('--[保存失败]：{}--'.format(e))
            return False

def name_processor(file_path):
    h5 = hashlib.md5()
    h5.update(file_path.encode('utf-8'))
    # 获得后缀
    file_suffix = os.path.splitext(file_path)[-1]
    name = h5.hexdigest() + file_suffix
    return name

if __name__ == '__main__':
    save_img('https://p3a.pstatp.com/weili/l/189459245242253771.jpg', './scense.jpg')