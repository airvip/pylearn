#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', seq=[1,2,3])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['name']=='air' and request.form['pass']=='123':
            return render_template('success.html', name=request.form['name'])
        return render_template('login.html', msg = '未知的用户名和密码！')

if __name__ == '__main__':
    app.run()