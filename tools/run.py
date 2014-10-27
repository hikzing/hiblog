#!/usr/bin/env python
# coding:utf-8
import _env
import tornado.web
import tornado.ioloop
from tornado.options import define, options
from hiblog._base.app import app

define("port", default=8000, help="develop mode with given port", type=int)


def run():
    tornado.options.parse_command_line()
    APP = tornado.web.Application(app.handlers, **app.setting)
    APP.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    run()
