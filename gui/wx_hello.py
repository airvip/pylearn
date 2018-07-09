#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title="",size=(300, 200)):
        super(Mywin, self).__init__(parent=parent, title=title, size=size)
        self.SetMaxSize(wx.Size(300, 200))
        self.init_ui()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)

        # 创建一个垂直方向的BoxSizer
        vbox = wx.BoxSizer(orient=wx.VERTICAL)

        label = wx.StaticText(panel, -1, label="Hello, world!")
        vbox.Add(label, flag=wx.TOP|wx.ALIGN_CENTER_HORIZONTAL)

        quit_btn = wx.Button(panel, -1, label='quit')
        quit_btn.SetForegroundColour('#FF0000')
        self.Bind(wx.EVT_BUTTON, handler=self.close_now, source=quit_btn)
        vbox.Add(quit_btn, flag=wx.ALIGN_CENTER_HORIZONTAL)

        panel.SetSizer(vbox)

    def close_now(self, event):
        self.Close(True)

app = wx.App(False)
win = Mywin(None, title='hi')
app.MainLoop()

