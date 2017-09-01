#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/2 1:52.

from multiprocessing import Pipe,Process
# import multiprocessing
# import pipes


def f(conn):
    conn.send([42,None,'Hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn , child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()