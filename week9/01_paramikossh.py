#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/25 16:56.

#请先安装paramiko

import paramiko
#创建ssh对象
ssh = paramiko.SSHClient()
#允许链接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#链接服务器
ssh.connect(hostname="localhost",port=22,username="newdyt",password="123")
#执行命令
stdin,stdout,stderr = ssh.exec_command("df")
#获取命令结果
result = stdout.read()
#关闭连接
ssh.close()