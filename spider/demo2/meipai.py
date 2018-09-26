# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:20

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import base64
import airutils
import re


class Decode(object):
    def getHex(self, param1):
        return {
            'str': param1[4:],
            'hex': ''.join(list(param1[:4])[::-1]),
        }

    def getDecimal(self, param1):
        loc2 = str(int(param1, 16))
        return {
            'pre': list(loc2[:2]),
            'tail': list(loc2[2:]),
        }

    def substr(self, param1, param2):
        loc3 = param1[0: int(param2[0])]
        loc4 = param1[int(param2[0]): int(param2[0]) + int(param2[1])]
        return loc3 + param1[int(param2[0]):].replace(loc4, "")

    def getPosition(self, param1, param2):
        param2[0] = len(param1) - int(param2[0]) - int(param2[1])
        return param2

    def decode(self, code):
        dict0 = self.getHex(code)
        dict1 = self.getDecimal(dict0['hex'])
        str0 = self.substr(dict0['str'], dict1['pre'])
        res_str = self.substr(str0, self.getPosition(str0, dict1['tail'])).encode('UTF-8')
        missing_padding = 4 - len(res_str) % 4
        if missing_padding:
            res_str += b'=' * missing_padding
        try:
            return base64.b64decode(res_str).decode()
        except Exception as e:
            print(e)
            print(dict0)



def meipai(keywords, pages=3):
    img_cnt = 0
    driver=webdriver.Chrome()
    driver.maximize_window()
    url = 'http://www.meipai.com/square/{}'.format(keywords)
    driver.get(url)
    for page in range(pages):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(random.randint(1, 4))
        items = driver.find_elements_by_class_name('content-l-video')
        for item in items:
            src = item.get_attribute('data-video')
            # print(src)
            if not src:
                continue
            true_src = Decode().decode(src)
            print(true_src)
            if None == true_src:
                continue
            filename = airutils.name_processor(re.search('com\/(.*)\?k',true_src).group(1))
            # filename = re.search('com\/(.*)\?k',true_src).group(1)
            path = 'D:/spider/meipai'
            res = airutils.save_img(img_url=true_src, file_name=filename, file_path=path)
            img_cnt += 1
            if res:
                print('第{}份资源{}保存成功...'.format(img_cnt, filename))
            else:
                print('第{}份资源{}保存失败...'.format(img_cnt, filename))


    driver.close()

if __name__ == "__main__":
    dict = {
        '搞笑':13,
        '爱豆':16,
        '高颜值':474,
        '舞蹈':63,
        '精选':488,
        '音乐':62,
        '美食':59
    }
    meipai(dict['舞蹈'] ,pages=3)
    # res = Decode().decode('aHR0cDovL212dmlkZW8xMC5tZWl0dWRhdGEuY29tLzViYTQ2OGRmODk3NTY4ODM4Lm1wND9rPTI1NBYTFhMDYxY2E2YzI3MWM4MQyY2U2NU1OGEwJnQ9NWJhZNhYzQ')
    # print(res)
    # res = re.search('com\/(.*)\?k','http://mvvideo10.meitudata.com/5ba7690cb47dd4603.mp4?k=fa097fdfc5ca8b3508f6c6ee4c0d80b0&t=5baf22a7').group(1)
    # print(res)