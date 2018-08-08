#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<b>欢迎进入Flask的世界!</b>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''<form action="/login" method="post">
        昵称：<input type="text" name="name"/><br/>
        密码：<input type="password" name="pass"/><br/>
        <button type="submit">登录</button>
        </form>'''
    else:
        if request.form['name']=='air' and request.form['pass']=='123':
            return '<b>登录成功 air!</b>'
        return '<b>未知的用户名和密码！</b>'

if __name__ == '__main__':
    app.run()