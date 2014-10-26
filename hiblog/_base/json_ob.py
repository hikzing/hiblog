#!/usr/bin/env python
# coding:utf-8

# from json import dumps
from yajl import dumps


class JsOb(dict):

    """ 修改后的字典类, 可以使用如obj.attr的用法

    用于模拟json对象
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


class StripJsOb(JsOb):

    """ 去除 Json 对象的前后空白, 返回新的 Json对象

    常用于处理用户的表单输入
    """

    def __init__(self, *args, **kwds):
        super(StripJsOb, self).__init__(*args, **kwds)
        for k, v in self.items():
            if isinstance(v, basestring):
                if not v.endswith('\n'):  # 保留换行符
                    _v = v.strip()
                else:
                    _v = v.lstrip()
                if _v != v:
                    self[k] = _v


if __name__ == '__main__':
    # d = {'a':1, 'b':2}
    d = JsOb(a='12 ', b=' ab          ', c=' dad\n')
    print(StripJsOb(**d))
