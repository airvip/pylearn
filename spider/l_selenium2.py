#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
# ele = browser.find_element_by_id("kw")
# print(ele.get_attribute('class'))

ele = browser.find_element_by_css_selector('a.mnav')
print(ele.text)
print(ele.id)
print(ele.location)
print(ele.tag_name)
print(ele.size)

# print(browser.get_cookies())

browser.execute_script('alert("Open by selenium")')
# browser.close()

