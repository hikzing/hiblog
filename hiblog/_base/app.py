#!/usr/bin/env python
# coding:utf-8
import _env
import tornado.web
import tornado.ioloop
from os.path import dirname, abspath, join
from importlib import import_module


class Route:

    """ 用装饰器的形式收集 url 路径

    如:
        route = Route()

        @route('hello')
        class HelloHandler(RequestHandler):
            def get(self):
                self.write('hello, world')

    """

    def __init__(self, prefix=''):
        self.handlers = []
        self._prefix = prefix

    def __call__(self, url, **kwds):
        def _(cls):
            self.handlers.append((self._prefix + url, cls, kwds))
            return cls
        return _


class App:

    def __init__(self):
        self.setting = dict(
            static_path=abspath(join(dirname(__file__), "../html/static")),  # TODO
        )

    @property
    def handlers(self, view_name='view'):
        """ 返回所有在 view的_route_list里定义的route的 handlers.
        """
        ROUTE_LIST = import_module('view._route_list').ROUTE_LIST
        handlers = []
        for route in ROUTE_LIST:
            handlers.extend(import_module('{}.{}'.format(view_name, route)).route.handlers)
        return handlers

    def run(self, port=8888):
        app = tornado.web.Application(self.handlers, **self.setting)
        app.listen(port)
        tornado.ioloop.IOLoop.instance().start()


app = App()

if __name__ == '__main__':
    app.run()
