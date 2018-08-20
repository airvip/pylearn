#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

input = browser.find_element_by_id("kw")
input.send_keys('火影忍者')
time.sleep(5)
input.clear()
input.send_keys('海贼王')
button = browser.find_element_by_id('su')
button.click()
