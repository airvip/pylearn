#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/10 12:38.

from sqlalchemy import Table,Column,Integer,String,Enum,DATE,ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType,PasswordType

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

Base = declarative_base()



class Host(Base):
    __tablename__ = "host"
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = "host_group"
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)
    remote_users = relationship()

    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = "remote_user"
    __table_args__ = (UniqueConstraint('auth_type','username','password',name='_user_passwd_uc'))
    id = Column(Integer,primary_key=True)
    AuthTypes = [
        ('ssh-passwd','SSH/Password'),
        ('ssh-key','SSH/KEY')
    ]
    # auth_type = Column(Enum(0,1))
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username
    pass

class BindHost(Base):
    '''
    information
    host ip --- username web---group---
    '''
    __tablename__ = "bind_host"
    __table_args__ = (UniqueConstraint('host_id', 'group_id', 'remoteuser_id', name='_host_group_remoteuser_uc'))
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    group_id = Column(Integer,ForeignKey('group.id'))
    remoteuser_id = Column(Integer,ForeignKey('remote_usr.id'))

    host = relationship("Host",backref="bind_hosts")
    host_group = relationship("HostGroup",backref="bind_hosts")
    remote_user = relationship("RemoteUser",backref="bind_hosts")
    def __repr__(self):
        return "<%s -- %s -- %s>"%(self.host.ip,
                                   self.remote_user.username,
                                   self.host_group.user)

class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))

    def __repr__(self):
        return self.username

class AuditLog(Base):
    pass

