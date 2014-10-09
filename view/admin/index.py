#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.my_view import AdminView, BaseView


route = Route(prefix='/admin')


@route('/?')
class AdminIndex(AdminView):

    def get(self):
        pass


@route('/test')
class Test(BaseView):

    def get(self):
        self.render()
