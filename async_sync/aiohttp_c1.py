#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as response:
            print(response)
            print(response.history)
            res = await response.text()
            print(len(res))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
