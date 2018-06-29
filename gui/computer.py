#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/6/29 11:24.

from tkinter import *
import decimal

root = Tk()
root.title('计算器')
root.resizable(width=False, height=False)

result = op = None
store = []
varstring = StringVar() # 接收用户输入


class Btnvalue(object):
    global store, varstring, result, op
    def __init__(self, btn):
        self.type = btn

    def seting(self):
        store.append(self.type)
        varstring.set(''.join(store))
        print(store)

    def dot(self):
        if store.count('.') >= 1:
            pass
        else:
            if store == []:
                store.append('0')
            store.append('.')
            varstring.set(''.join(store))

    def clear(self):
        store.clear()
        varstring.set('')
        result = None
        op = None

    def plus_minus(self):
        global store
        if store == []:
            store = ['0']
        if store[0]:
            if store[0] == '-':
                del store[0]
            else:
                store.insert(0,'-')
        varstring.set(''.join(store))


    def compute(self):
        global store, varstring, result, op

        if varstring.get() != '':
            num1 = decimal.Decimal(varstring.get())
            if op == None:
                result = num1
            else:
                num1 = decimal.Decimal(result)
                num2 = decimal.Decimal(varstring.get())
                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    result = num1 / num2

            if self.type == '%':
                result = num1 / 100

            if self.type == '=':
                op = None
            else:
                op = self.type

            varstring.set(str(result))
            store.clear()




def display(root):
    # 第0行
    entry1 = Label(root, width=29, height=2, bg='#FFFFFF', anchor='se', textvariable=varstring)
    entry1.grid(row=0, columnspan=4)

    # 第一行
    btnC = Button(root, text=' C ', width=6, height=2, command=Btnvalue('c').clear) # 清除
    btnP_M = Button(root, text=' ± ', width=6, height=2, command=Btnvalue('c').plus_minus) # 正负
    btnPer = Button(root, text=' % ', width=6, height=2, command=Btnvalue('%').compute) # 百分号
    btnDiv = Button(root, text=' / ', width=7, height=2, bg="#FA8712", command=Btnvalue('/').compute) # 除号
    btnC.grid(row=1, column=0)
    btnP_M.grid(row=1, column=1)
    btnPer.grid(row=1, column=2)
    btnDiv.grid(row=1, column=3)

    # 第二行
    btn7 = Button(root, text=' 7 ', width=6, height=2, command=Btnvalue('7').seting)
    btn8 = Button(root, text=' 8 ', width=6, height=2, command=Btnvalue('8').seting)
    btn9 = Button(root, text=' 9 ', width=6, height=2, command=Btnvalue('9').seting)
    btnMul = Button(root, text=' * ', width=7, height=2, bg="#FA8712", command=Btnvalue('*').compute)
    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)
    btnMul.grid(row=2, column=3)

    # 第三行
    btn4 = Button(root, text=' 4 ', width=6, height=2, command=Btnvalue('4').seting)
    btn5 = Button(root, text=' 5 ', width=6, height=2, command=Btnvalue('5').seting)
    btn6 = Button(root, text=' 6 ', width=6, height=2, command=Btnvalue('6').seting)
    btnMin = Button(root, text=' - ', width=7, height=2, bg="#FA8712", command=Btnvalue('-').compute)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btnMin.grid(row=3, column=3)

    # 第四行
    btn1 = Button(root, text=' 1 ', width=6, height=2, command=Btnvalue('1').seting)
    btn2 = Button(root, text=' 2 ', width=6, height=2, command=Btnvalue('2').seting)
    btn3 = Button(root, text=' 3 ', width=6, height=2, command=Btnvalue('3').seting)
    btnAdd = Button(root, text=' + ', width=7, height=2, bg="#FA8712", command=Btnvalue('+').compute)
    btn1.grid(row=4, column=0)
    btn2.grid(row=4, column=1)
    btn3.grid(row=4, column=2)
    btnAdd.grid(row=4, column=3)

    # 第五行
    btn0 = Button(root, text=' 0 ', width=14, height=2, command=Btnvalue('0').seting)
    btnDot = Button(root, text=' . ', width=6, height=2, command=Btnvalue('.').dot)
    btnEq = Button(root, text=' = ', width=7, height=2, bg="#FA8712", command=Btnvalue('=').compute)
    btn0.grid(row=5, column=0, columnspan=2)
    btnDot.grid(row=5, column=2)
    btnEq.grid(row=5, column=3)


display(root)

root.mainloop()