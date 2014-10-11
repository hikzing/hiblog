#!/usr/bin/env python
# coding:utf-8

# from json import dumps
from yajl import dumps


class JsOb(dict):

    """ 修改后的字典类, 可以使用如obj.attr的用法

    常用于模拟json对象
    """

    def __init__(self, *args, **kwds):
        for a in args:
            self[a] = None
        self.update(**kwds)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __iter__(self):
        return self.iteritems()

    def __str__(self):
        return dumps(self)  # 能显示中文
