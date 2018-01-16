#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/1/16 16:23.

import imaplib
#导入解析邮件模块
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#收取邮件用户的账户与密码
_email = '980062449@qq.com'
_pass  = 'glgzzbaviqmbbeaj'


#pop3服务器
imap_server = 'imap.qq.com'
imObj = imaplib.IMAP4(imap_server)
# 登录账户
imObj.login(_email,_pass)
# 选择邮箱。返回是一个元组，默认邮箱是“收件箱”的邮件数。
mylist = imObj.select()
#打印返回的信息
print("获取 : %s，邮件：%s" %(mylist[0],mylist[1][0].decode()))
#typ, data = imObj.search(None, 'ALL')
if int(mylist[1][0].decode()) > 0:
    #读取第一封
    typ, data = imObj.fetch(mylist[1][0].decode(), '(RFC822)')
    # 获取邮件原始文本
    msg_content = data[0][1].decode('utf-8')
    # 解析html
    content = Parser().parsestr(msg_content)
    # 打印源码
    print(content)

imObj.close()
imObj.logout()

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