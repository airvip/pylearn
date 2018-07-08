#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title="",size=(600, 400)):
        super(Mywin, self).__init__(parent=parent, title=title, size=size)
        self.panel = wx.Panel(self, -1)
        self.Show()
        self.create_widgets()

    def create_widgets(self):
        self.label = wx.StaticText(self.panel, -1, label="Hello, world!", size=(600, 30), style=wx.ALIGN_CENTRE)

        self.quit_btn = wx.Button(self.panel, -1, label='quit', pos=(30,30))
        self.quit_btn.SetForegroundColour('red')
        self.Bind(wx.EVT_BUTTON, handler=self.close_now, source=self.quit_btn)


    def close_now(self, event):
        self.Close(True)

app = wx.App(False)
win = Mywin(None, title='hi')
app.MainLoop()


# app = wx.App(False) # 实例化应用对象
# win = wx.Frame(None, title='hi', size=(200, 100)) # 创建窗体
# panel = wx.Panel(win)
# wx.StaticText(parent=panel, label="Hello, world!")
# win.Show()
# app.MainLoop() # 运行程序