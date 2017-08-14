#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/5 17:35.

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffie',31),
    ('book',100),
]
tmp_car = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        #for item in product_list:
        #     print(product_list.index(item),item)
        for i,v in enumerate(product_list):
            print(i,v)
        user_choice = input("do you buy:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:#can buy
                    tmp_car.append(p_item)
                    salary  -= p_item[1]
                    print("Added \033[32;1m%s\033[0m into shopping car,your balance is  \033[31;1m%s\033[0m" %(p_item[0],salary))
                else:
                    print("\033[41;1mYour current salary  is [%s],can not buy\033[0m"%(salary))
            else:
                print('production code [%s] is not exist!' %user_choice)
        elif user_choice == 'q':
            print('-----------shopping list---------')
            for p in tmp_car:
                print(p)
            print("your current balance:",salary)
            break
        else:
            print("invalid option")
else:
    print("invalid salary")