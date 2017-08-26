#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/25 16:56.

#请先安装paramiko

import paramiko
#创建ssh对象
transport = paramiko.Transport("localhost",22)
#链接服务器
transport.connect(username="newdyt",password="123")
sftp = paramiko.SFTPClient.from_transport(transport)
#讲info上传至服务器/tmp/test.txt
sftp.put("./info","/tmp/test.txt")
#讲remove_path下载到本地
sftp.get("remove_path","localhost_path")
#关闭连接
transport.close()