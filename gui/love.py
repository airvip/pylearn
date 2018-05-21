#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox

tk = Tk()

tk.title("是否喜欢我")  # 设置设置窗口标题
tk.geometry("600x400")  # 设置窗口大小
tk.resizable(width=False, height=False)  # 设置窗口是否可以改变长 宽
tk.minsize(width=False, height=False)

tk.protocol('WM_DELETE_WINDOW', False)

def love_me():
    res = tkinter.messagebox.askyesno(title='妹纸', message="妹纸,是不是喜欢我！")
    if res == True:
        tk.quit()
    else:
        tkinter.messagebox.showinfo(title='妹纸', message="妹纸，只能喜欢我！")
    # print(res)


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
    # print("root现在的位置是", event.x_root, event.y_root)
    # print("winfo_root现在的位置是", tk.winfo_rootx(), tk.winfo_rooty())
    # print("winfo_vroot现在的位置是", tk.winfo_vrootx(), tk.winfo_vrooty())
    # print("winfo现在的位置是", tk.winfo_x(), tk.winfo_y())
    if tk.winfo_rootx() + 370 < event.x_root < tk.winfo_rootx() + 460 and tk.winfo_rooty() + 180 < event.y_root < tk.winfo_rooty() + 220:
        btn2.place(x=400, y=50)
    else:
        btn2.place(x=400, y=190)


tk.bind("<Motion>", call_back)

tk.mainloop()
