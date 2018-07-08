#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
conn = redis.StrictRedis(connection_pool=pool)

res = conn.set('name', 'airvip', 5)
print(res)

print(conn.get('name').decode())



