#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/12 17:17.

#导入获取邮件pop模块
import poplib
#导入解析邮件模块
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#收取邮件用户的账户与密码
_email = '99@qq.com'
_pass  = 'glgeaj'
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
# index表示邮件列表索引
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
#retr(index):获取详细 index,(返回信息, 消息 index 的所以内容, 消息的字节数)
#lines是个列表
resp, lines, octets = popObj.retr(index)
#获取邮件原始文本
msg_content =  b'\r\n'.join(lines).decode("utf-8")
#解析html
content = Parser().parsestr(msg_content)
#打印源码
print(content)
# 关闭连接:
popObj.quit()

#解码函数
def s_decode(s):
    #只解析第一个，decode_header返回一个列表
    val,charset = decode_header(s)[0]
    if charset:
        val = val.decode(charset)
    return val

#解析邮件头部
def print_header(content):
    for header in [ 'Subject','From','Date' ,'To']:
        val = content.get(header,'')
        if val:
            if header == 'Subject' or header == 'Date':
                val = s_decode(val)
            else:
                #解析email地址串，parseaddr 返回一个元组
                name,email = parseaddr(val)
                name = s_decode(name)
                val = '%s <%s>' %(name,email)
        print('%s:%s'%(header,val))

#获取内容字符集
def content_charset(content):
    charset = content.get_charset()
    if charset is None:
        content_type = content.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

#解析邮件内容
def print_content(content):
    if (content.is_multipart()):
        parts = content.get_payload()
        for n, part in enumerate(parts):
            # print(n,part)
            print_content(part)
    else:
        content_type = content.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            charset = content_charset(content)
            content = content.get_payload(None,True)
            if charset:
                content = content.decode(charset)
            print('Text: %s' % content)
        else:
            print('Attachment: %s' % content_type)

#邮件打印
print_header(content)
print_content(content)