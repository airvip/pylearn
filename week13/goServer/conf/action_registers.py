#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/15 0:18.


from modules import views

actions = {
    "syncdb":views.syncdb,
    "create_users":views.create_users,
    "create_groups":views.create_groups,
    "create_hosts":views.create_hosts,
    "create_remoteusers":views.create_remoteusers,
}