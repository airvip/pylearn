#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/2/23 10:00.

import requests
from wxpy import *
import json

bot = Bot(cache_path=True)

def talks_robot(info = '在吗?'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '6b1*****ed'
    data = {'key': apikey, 'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys

@bot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_robot(info=message)
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息内容和类型
        return replys

bot.start()
embed()

