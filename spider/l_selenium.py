#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
# print(browser.page_source)
# browser.close()




head1 = browser.find_element_by_id("head")  # id 为 head
head2 = browser.find_element_by_css_selector("#head")  # css 选择器
head3 = browser.find_element_by_xpath('//div[@id="head"]')  # xpath 选择器
print(head1)
print(head2)
print(head3)

browser.close()