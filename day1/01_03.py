#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 9:28.

msg = """
name = "你好 ,世界"
print(name)
"""

print(msg)

name = input("What is your name ?")
password = input("enter your password ?")
print("my name is ",name)
print("password is ",password)


name = input("your name:")
age = int(input("your age:"))
job = input("your job:")

info = """
--------- info of %s ---------
name:%s
age:%d
job:%s
"""%(name,name,age,job)


print(info )

info2 = """
--------- info of {_name} ---------
name:{_name}
age:{age}
job:{job}
""".format(_name=name,age=age,job=job)
print(info2)

info3 = """
--------- info of {0} ---------
name:{0}
age:{1}
job:{2}
""".format(name,age,job)
print(info3)