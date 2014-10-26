#!/usr/bin/env python
# coding:utf-8
import _env
from _base.app import Route
from _base.controller import BaseView
from _base.config import Config
from model.blog import blog_lists, blog_by_slug_name, blog_count
from model.my_markdown import turn_to_markdown
from tornado.web import HTTPError


route = Route()


@route('/')
class Index(BaseView):

    blog_limit = 8  # 主页展示的文章数量

    def get(self):
        offset = int(self.get_argument('p', 1)) - 1
        limit = self.blog_limit

        return self.render(
            blogs=[o.detail_dumps for o in blog_lists(offset * limit, limit)],
            total=blog_count(),           # 分页用: blog的总数.
            limit=limit                   # 分页用: 每页的显示数.
        )


@route('/blog/(.+)')
class Post(BaseView):

    def get(self, blog_name):

        blog = blog_by_slug_name(blog_name)
        if blog:
            return self.render(
                title='{} | article'.format(Config.host),
                blog_title=blog.title,
                author=blog.author,
                post_date=blog.post_date,
                content=turn_to_markdown(blog.content),
                author_page=blog.author_page or '',
            )
        else:
            raise HTTPError(404)


@route('/about')
class About(BaseView):

    def get(self):
        return self.render()


@route('/about/me')
class Resume(BaseView):

    def get(self):
        return self.render()


@route('/contact')
class Contact(BaseView):

    def get(self):
        return self.render()


if __name__ == '__main__':
    pass
