#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.controller import AdminView, LoginView
from _base.config import Config
from _base.json_ob import JsOb
from model.blog import blog_lists, blog_count, Blog
from model.msg import msg_unread_list, msg_count, msg_lists


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    blog_limit = 2

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
            data.author = data.title = data.content = ''
        else:  # 编辑状态
            data.author = blog.author
            data.title = blog.title
            data.content = blog.content

        self.render(data=data)


@route('/msg')
class Msg(AdminView):

    msg_limit = 0

    def get(self):

        offset = int(self.get_argument('p', 1)) - 1
        limit = self.msg_limit

        self.render(
            msgs=[o.msg_info_dumps for o in msg_lists(offset, limit)],
            total=msg_count(),
            limit=limit
        )
