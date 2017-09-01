#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/2 1:52.

from multiprocessing import Pipe,Process
# import multiprocessing
# import pipes


def f(conn):
    conn.send([42,None,'Hello'])
    conn.send([42,None,'Hello1'])
    print("from parent:",conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn , child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send(("i","am","a","boy"))
    p.join()