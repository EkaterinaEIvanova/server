from aiohttp import web
from threading import Lock


class Handler:

    def __init__(self):
        self.counter = 0

    async def handle(self, request):
        with Lock():
            self.counter += 1
        return web.Response(text=f'{self.counter}')


handler = Handler()
app = web.Application()
app.add_routes([web.get('/count', handler.handle)])
web.run_app(app)
