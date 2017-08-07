#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/7 9:38.

#data = open("03_02_file",encoding="utf-8").read()
'''
#file open only read
f = open("03_02_file_0","r",encoding="utf-8")
data = f.read()
f.close()
print(data)

#file only write
f = open("03_02_file_1","w",encoding="utf-8")
f.write("我爱北京天安门\n")
f.write("天安门上太阳升\n")
f.close()

#file append only write
f = open("03_02_file_1","a",encoding="utf-8")
f.write("when i was young i listen to the radio\n")
f.write("天安门上太阳升\n")
f.close()

f = open("03_02_file_0","r",encoding="utf-8")
for i in range(5):
    print(f.readline().strip())
f.close()

#low  loop
f = open("03_02_file_0","r",encoding="utf-8")
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("line".center(50,"*"))
        continue
    print(line.strip())
f.close()

#high biger
f = open("03_02_file_0","r",encoding="utf-8")
count = 0
for line in f:
    count += 1
    if count == 9:
        print("line".ljust(20,"*"))
        continue
    print(line.rstrip())
f.close()

'''

#read method can use utf-8 but in seek method a chinese char is three bytes
f = open("03_02_file_0","r",encoding="utf-8")
print(f.tell())
print(f.read(1))
print(f.tell())
f.seek(3)
print(f.readline())

print(f.encoding)
print(f.fileno())
print(f.isatty())
f.close()


'''
打开文件的模式有：
r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件
r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
rU
r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
rb
wb
ab
'''