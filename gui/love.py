#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox

tk = Tk()

tk.title("女朋友")  # 设置设置窗口标题
tk.geometry("600x400")  # 设置窗口大小
tk.resizable(width=False, height=False)  # 设置窗口是否可以改变长 宽


def love_me():
    tkinter.messagebox.showinfo(title='妞', message="妞,老子就知道你喜欢我!")


Button(tk, text="喜欢我", command=love_me).place(x=150, y=190, anchor=NW)
btn2 = Button(tk, text="不喜欢我")
btn2.place(x=400, y=190, anchor=NW)

'''
win_w = tk.winfo_x()
win_y = tk.winfo_y()
print(win_w, win_y)


def change(event):
    tk.update()
    print("x", tk.winfo_x(), "y", tk.winfo_y())


tk.bind("<Configure>", change)  # 绑定事件
'''


def call_back(event):
    print("现在的位置是", event.x_root, event.y_root)
    if 367 < event.y_root < 410 and 568 < event.x_root < 627:
        btn2.place(x=400, y=50)
    else:
        btn2.place(x=400, y=190)


tk.bind("<Motion>", call_back)

tk.mainloop()
