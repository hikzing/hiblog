#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.controller import AdminView, LoginView
from _base.config import Config


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    def get(self):
        self.render()


@route('/logout')
class Logout(LoginView):

    def get(self):
        self.clear_cookie('auth')
        self.redirect('//%s' % Config.host)
