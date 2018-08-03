#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(encoding='UTF-8')

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.baidu.com')
        print(len(html))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [ main() for i in range(10) ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
