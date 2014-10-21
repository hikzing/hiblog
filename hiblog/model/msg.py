#!/usr/bin/env python
# coding:utf-8
import _env
from _base.json_ob import JsOb
from model.db import Doc
from time import time, strftime, localtime


class Msg(Doc):

    structure = dict(
        user_name=basestring,
        user_mail=basestring,
        content=basestring,
        _create_time=int,
        has_read=bool,
    )

    @property
    def post_time(self, format_="%Y-%m-%d"):
        return strftime(format_, localtime(self._create_time))

    @property
    def msg_summarize(self, length=30):
        content = str(self.content)
        return '%s...' % content[:length] if content else ''  # TODO: may be there is a better way

    @property
    def msg_info_dumps(self):
        o = JsOb()
        for each in self.structure:
            setattr(o, each, getattr(self, each))
        o._id = self._id
        o.post_time = self.post_time

        return o


def msg_new(user_name, user_mail, msg):
    o = Msg()

    o.user_name = user_name
    o.user_mail = user_mail
    o.content = msg
    o._create_time = time()
    o.has_read = False

    o.save()


def msg_lists(offset=0, limit=0):
    return Msg.find(sort=[('has_read', 1)], limit=limit, skip=offset)


def msg_unread_list(offset=0, limit=0):
    return Msg.find(dict(has_read=False), limit=limit, skip=offset)


def msg_unread_count():
    return Msg.count(dict(has_read=False))


def msg_count():
    return Msg.count()


def msg_read(_id):
    msg = Msg.find_one(_id)
    msg.has_read = True
    msg.save()


def msg_read_all():
    for msg in Msg.find():
        msg.has_read = True
        msg.save()

if __name__ == '__main__':
    print(msg_lists()[0]._id))
