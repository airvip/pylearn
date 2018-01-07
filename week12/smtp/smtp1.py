#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送者的邮箱
_from = '949@qq.com'
_pass = 'bf'
# 接收者的邮箱，可以设置多个，参数是个列表
_to = ['sdqhwzb@qq.com']
#MIMEText 三个参数：
#第一个为邮件正文内容
#第二个 plain 设置文本格式，最终的MIME就是'text/plain'
#第三个 utf-8 设置编码，这也是现在大多数编程使用的编码
message = MIMEText('好久没有联系了，现在必须使用一些标准的语法文字来给你聊天了。', 'plain', 'utf-8')
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

