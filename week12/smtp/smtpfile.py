#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

#发送者邮箱
_from = '989@qq.com'
#发送者密码（授权码）
_pass = 'bcf'
#接收者邮箱
_to = ['sdqhwzb@qq.com']

#创建一个带附件的实例例
message = MIMEMultipart('base')
message['From'] = Header("阿尔维奇163", 'utf-8')
message['To'] =  Header("阿尔维奇", 'utf-8')
#添加主题
subject = '阿尔维奇最近都在忙什么？'
message['Subject'] = Header(subject, 'utf-8')

#message_content = MIMEMultipart('info')
info =  '''
<p style="color:red">好久没有联系了，现在必须使用一些标准的语法文字来给你聊天了。</p>
<p><a href="http://blog.diff.wang">新的博客地址</a></p>
<p><img src="cid:image"></p>
'''
#message_content.attach(MIMEText(info, 'html', 'utf-8'))
message.attach(MIMEText(info, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('./test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image>')
message.attach(msgImage)


# 构造附件，发送当前目录下的 test.txt 文件
ff = open('./test.txt','rb').read()
attr = MIMEText(ff,'base64','utf-8')
fp.close()
#设置内容类型
attr["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
attr["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(attr)

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