#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379)

res = conn.delete('name')
print(res)
