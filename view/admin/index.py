#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.my_view import BaseView


route = Route(prefix='/admin')


@route('/')
class Index(BaseView):

    def get(self):
        self.write('hello, i am admin')
