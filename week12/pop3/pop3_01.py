#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/12 17:17.

import poplib
from email.parser import Parser

#收取邮件用户的账户与密码
_email = '980062449@qq.com'
_pass  = ''


#pop3服务器
pop_server = 'pop.qq.com'
popObj = poplib.POP3(pop_server)
# 设置调试模式，可以看到与服务器的交互信息
popObj.set_debuglevel(1)
# 向服务器发送用户名
popObj.user(_email)
# 向服务器发送密码
popObj.pass_(_pass)
# 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
mylist = popObj.stat()
#打印返回的信息
print("邮件：%s,字节：%s" %(mylist[0],mylist[1]))

# list()返回所有邮件的编号:(返回信息, 消息列表, 消息的大小)
resp, mails, octets = popObj.list()
#print(mails)

# index表示邮件列表索引
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)

#retr(index):获取详细 index,(返回信息, 消息 index 的所以内容, 消息的字节数)
#lines是个列表
resp, lines, octets = popObj.retr(index)
print(lines)

#获取邮件原始文本
msg_content =  b'\r\n'.join(lines).decode("utf-8")
#解析html
content = Parser().parsestr(msg_content)
print(content)
