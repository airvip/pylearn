#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    name = request.match_info.get('name', "Python")
    text = "Hello, " + name
    return web.Response(text=text)


async def main(loop):
    app = web.Application(loop=loop)
    app.add_routes(routes)
    resp = await loop.create_server(app.make_handler(), host='127.0.0.1', port=8888)
    return resp

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()

