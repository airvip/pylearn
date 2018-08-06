#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
@routes.get('/{name}')
async def hello(request):
    name = request.match_info.get('name', "Python")
    text = "Hello, " + name
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=8888)

