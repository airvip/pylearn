#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/25 16:56.

#请先安装paramiko

import paramiko

private_key = paramiko.RSAKey.from_private_key_file("/home/auto/.ssh/id_rsa")
#创建ssh对象
ssh = paramiko.SSHClient()
#允许链接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#链接服务器
ssh.connect(hostname="localhost",port=22,username="newdyt",pkey=private_key)
#执行命令
stdin,stdout,stderr = ssh.exec_command("df;ifconfig")
#获取命令结果
# result = stdout.read()
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())
#关闭连接
ssh.close()