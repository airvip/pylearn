#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<p name="info" class="title"><b>p The Dormouse's story<span>123</span></b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> ;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</html>
"""

# soup = BeautifulSoup(html_doc, features="html.parser")
soup = BeautifulSoup(html_doc, features="lxml")


# print(soup.prettify())

'''
# 标签选择
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)

# 标签名
print(soup.title.name)

# 获取标签属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p.attrs['class'])

# 获取标签内容
print(soup.p.string)

# 嵌套获取标签内容
print(soup.head.title.string)

# 子节点
print(soup.p.contents)

for i in soup.p.children:
    print(i)

# 子孙节点
for i in soup.p.descendants:
    print(i)

# 父节点和祖先节点
print(soup.b.parent)
for i in soup.b.parents:
    print(i)

print(soup.find('p'))
print(soup.find(attrs={'name':'info'}))
print(soup.find(text='...'))


print(soup.select('title'))
print(soup.select('.title'))
print(soup.select('#link1'))
'''

print(soup.select('p > a'))
print(soup.select('p #link1'))

print(soup.select("p[name='info']"))

for i in soup.select('p > a'):
    print(i.get_text())

for i in soup.select('p > a'):
    print(i['id'])

for i in soup.select('p > a'):
    print(i.attrs['id'])
