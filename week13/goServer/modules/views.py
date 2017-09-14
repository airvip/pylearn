#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/14 23:48.

from models import models
from conf import settings

def syncdb(argvs):
    print("syncind DB...")
    engine = models.create_engine(settings.ConnParams,echo=True)
    models.Base.metadata.create_all(engine)#创建所有表结构






















