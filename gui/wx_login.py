#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wx


class Login(wx.Frame):
    def __init__(self, parent, title="",size=(250, 160)):
        super(Login, self).__init__(parent=parent, title=title, size=size)
        self.SetMaxSize(wx.Size(250, 160))
        self.init_ui()
        self.Center()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)

        # 创建 垂直尺寸管理器 : 用来管理接下来的 水平管理器 和 其他组件
        vbox = wx.BoxSizer(orient=wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        user_label = wx.StaticText(panel, label='用户:')
        self.user_text = wx.TextCtrl(panel)

        hbox1.Add(user_label, flag=wx.RIGHT, border=5)
        hbox1.Add(self.user_text, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        pwd_label = wx.StaticText(panel, label='密码:')
        self.pwd_text = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        hbox2.Add(pwd_label, flag=wx.RIGHT, border=5)
        hbox2.Add(self.pwd_text, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(panel, label="登录")
        hbox3.Add(btn)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        self.Bind(wx.EVT_BUTTON, handler=self.check, source=btn)

        panel.SetSizer(vbox)

    def check(self, event):
        user_dict = {'airvip': '123456', 'lucy': '123456'}  # 模拟数据库中的数据
        # 账号验证
        if self.user_text.GetValue() in user_dict.keys() and user_dict[self.user_text.GetValue()] == self.pwd_text.GetValue():
            dig = wx.MessageDialog(None, message='欢迎 %s, 成功登录' % self.user_text.GetValue(), caption='登陆成功', style=wx.OK )
            res = dig.ShowModal() # 显示对话框
            if wx.ID_OK == res: # wx.ID_OK === 5100
                self.Close(True)
        else:
            res = wx.MessageBox(message='登录失败', caption='登陆失败', style=wx.OK)
            if wx.OK == res:
                self.user_text.SetValue('')
                self.pwd_text.SetValue('')



app = wx.App(False)
win = Login(None, title='login')
app.MainLoop()

