#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

_from = '949@qq.com'
_pass = 'bmf'
_to = ['sdqhwzb@qq.com']

#仅在此处稍作修改即可
info =  '''
<p style="color:red">好久没有联系了，现在必须使用一些标准的语法文字来给你聊天了。</p>
<p><a href="http://blog.diff.wang">新的博客地址</a></p>
'''
message = MIMEText(info, 'html', 'utf-8')
message['From'] = Header("阿尔维奇163", 'utf-8')
message['To'] =  Header("阿尔维奇", 'utf-8')
#添加主题
subject = '阿尔维奇最近都在忙什么？'
message['Subject'] = Header(subject, 'utf-8')
#发送测试
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.qq.com', 25)  # 25 为 SMTP 端口号
    smtpObj.login(_from, _pass)
    smtpObj.sendmail(_from, _to, message.as_string())
    print ("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print ("Error: %s" % e)