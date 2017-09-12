#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/10 12:38.

from sqlalchemy import Table,Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class HostGroup(Base):
    pass

class RemoteUser(Base):
    pass

class UserProfile(Base):
    pass

class AuditLog(Base):
    pass

