#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/15 23:47.


from sqlalchemy import create_engine,Table
from sqlalchemy.orm import sessionmaker

from conf import settings


engine = create_engine(settings.ConnParams)

SessionCls = sessionmaker(bind=engine)
session = SessionCls()