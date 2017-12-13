#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/29 23:59.

import threading
import time


event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count>5 and count<=8:#改为红灯
            event.clear()#清除标志位
            print("\033[41;1mred light is on...\033[0m",count)
        elif count > 8:
            event.set()#变绿灯
            count = 0
            print("\033[42;1mgreen light is on...\033[0m", count)
        else:
            print("\033[42;1mgreen light is on...\033[0m",count)
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():#设置标志位为绿灯
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."%name)
            event.wait()
            print("\033[34;1m green light is on,[%s] start going...\033[0m"%name)

light = threading.Thread(target=lighter)
light.start()

car = threading.Thread(target=car,args=("bwm",))
car.start()

