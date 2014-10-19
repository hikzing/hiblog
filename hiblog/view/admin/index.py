#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.controller import AdminView, LoginView
from _base.config import Config
from model.blog import blog_lists, blog_count


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    blog_limit = 1

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
class Blog(AdminView):

    def get(self):
        is_new = self.get_arguments('new', None)
        blog_id = self.get_argument('blog_id', None)

        if is_new or not blog_id:
            return self.render()
        else:
            pass


@route('/msg')
class Msg(AdminView):

    def get(self):
        pass
