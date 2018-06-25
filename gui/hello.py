#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/25 14:17.

from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = Label(self, text='Hello, world!')
        self.hello_label.pack()

        self.quit_btn = Button(self, text='quit', fg="red", command=self.quit)
        self.quit_btn.pack()


root = Tk()
root.title('hi') # 设置窗口标题
root.geometry("200x100") # 设置窗口大小
app = App(root) # 实例化App
app.mainloop() # 主消息循环