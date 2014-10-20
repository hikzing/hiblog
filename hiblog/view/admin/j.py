#!/usr/bin/env python
# coding: utf-8
import _env
from _base.app import Route
from _base.controller import JsonErrView, JsonAdminView
from _base.json_ob import JsOb
from model.re_mail import RE_MAIL
from model.password import Password
from model.blog import Blog

import time

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
                err.password = '帐号或密码错误'
        self.render(err)


@route('/j/blog/save')
class BlogSave(JsonErrView, JsonAdminView):

    def post(self):
        o = self.json
        err = JsOb()

        if not o.author:
            err.author = "请输入作者名字"
        if not o.title:
            err.title = "请输入文章标题"
        if not o.content:
            err.content = "请输入内容"

        if not err:
            blog = Blog.find_one(dict(title=o.title), create_new=True)

            blog.author = o.author
            blog.title = o.title
            blog.content = o.content

            if not blog._date:
                blog._date = time.time()  # 只有新建blog时才更新日期
            blog.save()

        self.render(err)


@route('/j/blog/delete')
class BlogDelete(JsonAdminView):

    def get(self):
        self.finish()


@route('/j/blog/edit')
class BlogEdit(JsonAdminView):

    def get(self):
        self.finish()
