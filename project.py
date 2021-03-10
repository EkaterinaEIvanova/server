from aiohttp import web
from threading import Lock

class Handler:

    def __init__(self):
        self.counter = 0

    def safe_increment(self):
        Lock().acquire()
        self.counter += 1
        Lock().release()

    async def handle(self, request):
        self.safe_increment()
        return web.Response(text=f'{self.counter}')


handler = Handler()
app = web.Application()
app.add_routes([web.get('/count', handler.handle)])
web.run_app(app)
