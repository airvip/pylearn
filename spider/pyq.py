#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq

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
d = pq(html_doc)

'''
print(d('#link1'))
print(d('.title'))
print(d('.title b'))
print(d('title'))
print(d('title, a'))
print(d('p a'))
print(d('p[name]'))
print(d('p[name="info"]'))

print(d.find('a'))
print(d.find('p a'))
print(d('a').filter('#link1'))
print(d('a').filter('.sister'))
print(d('a').filter('.sister').eq(0))

print(d('span').parent())
print(d('span').parents())

print(d('a').siblings())

print(d('#link1').next_all())

'''



print(d('p').attr('name'))
print(d('p.story').text())
print(d('p.story').html())




