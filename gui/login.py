#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/7/2 10:26.

from tkinter import *
from tkinter import messagebox

def check():
    user_dict = {'airvip': '123456', 'lucy': '123456'} # 模拟数据库中的数据
    # 账号验证
    if user.get() in user_dict.keys() and user_dict[user.get()] == passwd.get():
        res = messagebox.showinfo(title='登录成功', message='欢迎 %s, 成功登录' % user.get())
        if 'ok' == res:
            root.quit()
    else:
        messagebox.showerror(title='登录失败', message='请检查您的输入')



root = Tk()
root.title('登录')
root.geometry('230x150')
root.resizable(0, 0)  # 窗口大小固定

user = StringVar()
passwd = StringVar()

f1 = Frame().pack()
Label(f1, text='用户:').place(x=20, y=20)
Entry(f1, textvariable=user).place(x=60, y=20)
Label(f1, text='密码:').place(x=20, y=60)
Entry(f1, textvariable=passwd).place(x=60, y=60)
Button(f1, text="提交", command=check).place(x=40, y=100)


root.mainloop()