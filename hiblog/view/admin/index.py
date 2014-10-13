#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.my_view import AdminView, BaseView


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    def get(self):
        self.write('test')


@route('/logout')
class Logout(AdminView):

    def get(self):
        pass
