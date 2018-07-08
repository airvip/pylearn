#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis

conn = redis.Redis(host='127.0.0.1', port=6379)

res = conn.set('name', '阿尔维奇')
print(res)

data = conn.get('name')
print(data.decode())