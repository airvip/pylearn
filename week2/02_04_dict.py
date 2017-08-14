#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/6 0:09.

info = {
    'stu1101':'tenglan wu',
    'stu1102':'longze luola',
    'stu1103':'xiaoze maliya',
}

for i in info:
    print(i,info[i])

for i,v in info.items():
    print(i,v)



print(info)
print(info['stu1101'])
print(info.get('stu1104'))

print('stu1105' in info)

info['stu1101'] = '武藤兰'
info['stu1104'] = 'cangjingkong'


#del
del info['stu1101']
info.pop("stu1102")
info.popitem()
print(info)









