#!/usr/bin/env python
# coding: utf-8
import _env
from _base.app import Route
from _base.my_view import JsonView


route = Route()


@route('/j/tag')
class Tag(JsonView):

    def post(self):
        self.finish()


@route('/j/category')
class Category(JsonView):

    def post(self):
        self.finish()


@route('/j/post')
class Post(JsonView):

    def post(self):
        self.finish()


@route('/j/blog')
class Blog(JsonView):

    limit = 8

    def post(self):
        offset = self.get_argument('page', default=0)

