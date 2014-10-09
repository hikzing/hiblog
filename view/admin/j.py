#!/usr/bin/env python
# coding: utf-8
import _env
from _base.app import Route
from _base.my_view import JsonView


route = Route(prefix='admin')


@route('/j/admin/edit/save')
class EditSave(JsonView):

    def get(self):
        self.finish()


@route('/j/admin/edit/delete')
class EditDelete(JsonView):

    def get(self):
        self.finish()
