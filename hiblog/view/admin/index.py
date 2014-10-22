#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.controller import AdminView, LoginView
from _base.config import Config
from _base.json_ob import JsOb
from model.blog import blog_lists, blog_count, Blog
from model.msg import msg_count, msg_lists, Msg, msg_read


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    blog_limit = 5

    def get(self):
        offset = int(self.get_argument('p', 1)) - 1
        limit = self.blog_limit

        self.render(
            blogs=[o.detail_dumps for o in blog_lists(offset * limit, limit)],
            total=blog_count(),
            limit=limit
        )


@route('/logout')
class Logout(LoginView):

    def get(self):
        self.clear_cookie('auth')
        self.redirect('//%s' % Config.host)


@route('/blog/edit')
class BlogPage(AdminView):

    def get(self):
        is_new = self.get_arguments('new', None)
        blog_id = self.get_argument('blog_id', None)

        data = JsOb()
        blog = Blog.find_one(blog_id)
        if is_new or not blog_id or not blog:
            data.author = data.title = data.content = data._id = ''
        else:  # 编辑状态
            data.author = blog.author
            data.title = blog.title
            data.content = blog.content
            data._id = blog_id

        self.render(data=data)


@route('/msg_wall')
class MsgWall(AdminView):

    msg_limit = 8

    def get(self):

        offset = int(self.get_argument('p', 1)) - 1
        limit = self.msg_limit

        self.render(
            msgs=[o.msg_info_dumps for o in msg_lists(offset, limit)],
            total=msg_count(),
            limit=limit
        )


@route('/msg_wall/(\w+)')
class MsgInfo(AdminView):

    def get(self, msg_id):
        if msg_id:
            msg = Msg.find_one(msg_id)
            if msg:
                self.render(msg=msg.msg_info_dumps)
