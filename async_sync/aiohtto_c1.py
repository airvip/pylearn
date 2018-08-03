#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import aiohttp
# import asyncio



async with aiohttp.ClientSession() as session:
    async with session.get('http://httpbin.org/get') as resp:
        print(resp.status)
        print(await resp.text())
