#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis
import time

conn = redis.Redis(host='127.0.0.1', port=6379)

res = conn.set('addr', 'china', 5)
print(res)


for i in range(8):
    print('第 %s 次获取 addr 值为: %s' %(i, conn.get('addr')))
    time.sleep(1)

