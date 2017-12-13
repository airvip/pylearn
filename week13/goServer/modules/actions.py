#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/9/14 23:57.

from conf import action_registers
from modules import utils

def help_msg():
    '''
    print help msgs
    :return:
    '''
    print("\033[31;1mAvailable commands:\033[0m")
    for key in action_registers.actions:
        print("\t",key)

def excute_from_command_line(argvs):
    if len(argvs) > 2:
        help_msg()
        exit()
    if argvs[1] not in action_registers.actions:
        utils.print_err("command [%s] does not exist!"%argvs[1], quit=True)
    action_registers.actions[argvs[1]](argvs[1:])
















































