#!/usr/bin/env python
# coding: utf-8
import _env
from _base.app import Route
from _base.controller import JsonErrView
from _base.json_ob import JsOb
from model.re_mail import RE_MAIL
from model.msg import msg_new


route = Route()


@route('/j/contact')
class Contact(JsonErrView):

    def post(self):
        o = self.json
        err = JsOb()

        if not o.name:
            err.name = "Please enter your name"
        if not o.email:
            err.email = "Please enter your email"
        elif not RE_MAIL.match(o.email):
            err.email = "Not a valid email address"
        if not o.message:
            err.message = "Please enter your message"

        if not err:
            msg_new(o.name, o.email, o.message)

        self.render(err)
