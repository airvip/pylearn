#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/7 16:24.

"""
join() 函数
'sep'.join(seq) 以sep作为分隔符，将seq所有的元素合并成一个新的字符串
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
"""

# [('♡♡♡♡♡♡♡♡'[(x-y)%8] if( (x*0.05)**2+(y*0.1)**2-1 )**3 - (x*0.05)**2*(y*0.1)**3 <= 0 else' ') for x in range(-30,30) ]) for y in range(15,-15,-1) ]



# print('\n'.join([''.join([('lovelove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-25,25)])for y in range(12,-12,-1)]))
# print([''.join([('lovelove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])


xa = []
xa_s = -2.0

while xa_s <= 2:
    xa.append(round(xa_s,3))
    xa_s += 0.15

# print(xa)

ya = []
ya_s = 2.0

while ya_s >= -2:
    ya.append(round(ya_s,3))
    ya_s -= 0.15

# print(ya)



for y in ya:
    line = ''
    for x in xa:
        if ((x)**2 + (y)**2-1)**3 - (x)**2 * (y)**3 <= 0:
            line += '*'
        else:
            line += ' '
    print('\033[1;31;40m'+line+'\033[0m')
