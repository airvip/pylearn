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



def create_remoteuser(argvs):
    '''
    create hosts
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage,should be:\ncreate_remoteusers -f <the new remoteusers file>",quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.RemoteUser(username=val.get('username'),auth_type=val.get('auth_type'),password=val.get('password'))
            session.add(obj)
        session.commit()


def create_groups(argvs):
    '''
    create groups
    :return:
    '''
    if '-f' in argvs:
        group_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage,should be:\ncreate_groups -f <the new groups file>",quit=True)
    source = yaml_parser(group_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.HostGroup(name=key)
            # if val.get('bind_host'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            # if val.get('user_profiles'):
            #     user_profiles = common_filters.user_profiles_filter(val)
            #     obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()


def create_users(argvs):
    '''
    create hosts
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage,should be:\ncreate_users -f <the new users file>",quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.UserProfile(username=key,password=val.get('password'))
            # if val.get('groups'):
            #     groups = session.query(models.Group).filter(models.Group.name)
            #     if not groups:
            #         print_err("none of [%s] exist in group table."%val.get(''))
            #     obj.groups = groups
            # if val.get("bind_hosts"):
            #     bind_hosts = common_filters.bind_host_filter(val)
            #     obj.bind_hosts = bind_hosts
            session.add(obj)
        session.commit()



















