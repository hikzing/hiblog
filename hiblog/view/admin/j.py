#!/usr/bin/env python
# coding: utf-8
import _env
from _base.app import Route
from _base.controller import JsonView, JsonErrView
from _base.json_ob import JsOb
from model.re_mail import RE_MAIL
from model.password import Password

route = Route(prefix='/admin')


@route('/j/login')
class Login(JsonErrView):

    def post(self):

        err = JsOb()
        account = self.json.mail
        password = self.json.password

        if not account:
            err.account = '请输入帐号'
        elif not RE_MAIL.match(account):
            err.email = '请输入正确的帐号'
        if not password:
            err.password = '请输入密码'

        if not err:
            if Password.verify(account, password):
                self.set_session(account)
            else:
                err.password = "帐号或密码错误"
        self.render(err)


@route('/j/admin/blog/new')
class BlogNew(JsonView):

    def get(self):
        self.finish()


@route('/j/admin/blog/delete')
class BlogDelete(JsonView):

    def get(self):
        self.finish()


@route('/j/admin/blog/edit')
class BlogEdit(JsonView):

    def get(self):
        self.finish()
