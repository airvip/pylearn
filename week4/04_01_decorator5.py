#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/9 15:11.

#装饰器  嵌套函数  + 高阶函数
username,password = "airvip",'abc123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'local':
                user = input("Username:").strip()
                pwrd = input("Password:").strip()

                if user == username and pwrd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)  #
                    print("after authentication".center(40, "*"))
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == 'ldep':
                print("搞毛线ldep")
            else:
                print("\033[31;1mInvalid suth_type\033[0m")
        return wrapper
    return out_wrapper

def index():
    print("welcome to index page")

@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldep")
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()