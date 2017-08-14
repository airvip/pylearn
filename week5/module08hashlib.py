#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/14 17:24.

import hashlib
print("md5".center(50,"*"))
m = hashlib.md5()
m.update(b"123456")
print(m.hexdigest())

m.update("Hello你好".encode(encoding="utf-8"))
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"123456Hello")
print(m2.hexdigest())

print("sha1".center(50,"*"))
sh = hashlib.sha1()
sh.update(b"123456")
print(sh.hexdigest())

sh.update("Hello你好".encode(encoding="utf-8"))
print(sh.hexdigest())

sh2 = hashlib.sha1()
sh2.update(b"123456Hello")
print(sh2.hexdigest())

print("hmac".center(50,"*"))
import hmac

h = hmac.new(b"this is a new password")
print(h.digest())
print(h.hexdigest())

