#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/5 18:19.

name = "my \tname is {name} and i am {age} years old!"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.encode())
print(name.endswith("vip"))
print(name[name.find("name"):])
print(name.format(name="airvip",age=23))
print(name.format_map({'name':'airvip','age':23}))
print(name.isalnum())
print('ab123'.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.isdigit())
print(name.isidentifier())#is a var name
print(name.islower())
print('33'.isnumeric())
print(' '.isspace())
print('My Name Is'.istitle())
print('My Name Is'.isprintable())
print('My Name Is'.isupper())
print(','.join(['1','2','3']))
print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))
print(name.rjust(50,'*'))
print('Airvip\n'.rstrip())
print('\nAirvip'.lstrip())
print('   \nAirvip\n   '.strip())
p = str.maketrans("abcdef","123456")
print("air vip".translate(p))

print('airvip'.replace('i','I'))
print('airvip'.replace('i','I',1))
print('airvip'.rfind('i'))
print('air vip'.split(' '))