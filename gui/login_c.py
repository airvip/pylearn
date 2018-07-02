#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/7/2 14:26.

from tkinter import *
from tkinter import messagebox

class Login(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry('230x150')
        self.master.resizable(0, 0)
        self.pack()
        self.login_display()


    def login_display(self):
        Label(self.master, text='用户:').place(x=20, y=20)
        self.user = Entry(self.master)
        self.user.place(x=60, y=20)
        Label(self.master, text='密码:').place(x=20, y=60)
        self.passwd = Entry(self.master, show='*')
        self.passwd.place(x=60, y=60)
        Button(self.master, text="提交", command=self.check).place(x=40, y=100)

    def check(self):
        user_dict = {'airvip': '123456', 'lucy': '123456'}  # 模拟数据库中的数据
        # 账号验证
        if self.user.get() in user_dict.keys() and user_dict[self.user.get()] == self.passwd.get():
            res = messagebox.showinfo(title='登录成功', message='欢迎 %s, 成功登录' % self.user.get())
            if 'ok' == res:
                self.master.quit()
        else:
            messagebox.showerror(title='登录失败', message='请检查您的输入')


root = Tk()
root.title('登录')
app = Login(root)
app.mainloop()

