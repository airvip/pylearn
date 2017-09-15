#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/14 23:48.

from models import models
from conf import settings
from modules.utils import print_err,yaml_parser
from modules.db_conn import engine,session

def syncdb(argvs):
    print("syncind DB...")
    engine = models.create_engine(settings.ConnParams,echo=True)
    models.Base.metadata.create_all(engine)#创建所有表结构

def create_hosts(argvs):
    '''
    create hosts
    :return:
    '''
    if '-f' in argvs:
        hosts_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage,should be:\ncreate_host -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.Host(hostname=key,ip=val.get('ip'),port=val.get('port') or 22)
            session.add(obj)
        session.commit()




















