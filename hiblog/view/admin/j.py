#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.controller import JsonErrView, JsonAdminView
from _base.json_ob import JsOb
from model.re_mail import RE_MAIL
from model.password import Password
from model.blog import Blog
from model.msg import msg_read, msg_rm

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
            if Password.account_exist(account):
                if Password.verify(account, password):
                    self.set_session(account)
                else:
                    err.password = '密码错误'
            else:
                err.email = "帐号不存在"

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

            blog = Blog(dict(
                author=o.author,
                title=o.title,
                content=o.content
                )
            )

            if o._id:
                blog.upsert(o._id)        # 更新已有的blog
            else:
                blog._date = time.time()  # 添加日期并新建一个b
                blog.save()

        self.render(err)


@route('/j/blog/rm/(\w+)')
class BlogDelete(JsonAdminView):

    def post(self, id):

        if id:
            Blog.find_one(str(id)).delete()

        self.finish({})


@route('/j/msg/read/(\w+)')
class MsgRead(JsonAdminView):

    def post(self, id):

        if id:
            msg_read(id)

        self.finish({})


@route('/j/msg/del/(\w+)')
class MsgDel(JsonAdminView):

    def post(self, id):

        if id:
            msg_rm(id)

        self.finish({})
