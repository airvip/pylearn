#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/13 0:46.

import random
#in 0 - 1
x= random.random()
print(x)

# in 1,2,3
x = random.randint(1,3)
print(x)
#in 1,2
x = random.randrange(1,3)
print(x)
#
x = random.choice('airvip is a boy')
print(x)

x = random.sample('airvip is a boy',2)
print(x)

x = random.uniform(1,3)
print(x)

l = [1,2,3,4,5,6]
random.shuffle(l)
print(l)