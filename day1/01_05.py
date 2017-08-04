#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/4 10:20.

age_of_airvip = 24
count = 0
while True:
    count = count + 1
    if count > 3:
        print("more three,game over..")
        break
    guess_age = int(input("guess age:"))

    if guess_age == age_of_airvip:
        print("yes,you got it.")
        break
    elif guess_age > age_of_airvip:
        print("think smaller...")
    else:
        print("think bigger!")