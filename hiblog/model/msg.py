#!/usr/bin/env python
# coding:utf-8
import _env
from model.db import Doc, R, redis
from time import time, strftime, localtime


R_UNREAD_MSG_ZSET = R.UNREAD_MSG_ZSET()


class Msg(Doc):

    structure = dict(
        user_name=basestring,
        user_mail=basestring,
        msg=basestring,
        create_time=int
    )

    default_values = dict(
        create_time=time(),
    )

    @property
    def format_time(self, format_="%Y-%m-%d"):
        return strftime(format_, localtime(self.create_time))

    @property
    def msg_summarize(self, length=30):
        return '%s...' % self.msg[:length]  # TODO: may be there is a better way


def msg_new(user_name, user_mail, msg):

    _time = time()

    o = Msg()
    o.user_name = user_name
    o.user_mail = user_mail
    o.msg = msg
    o.create_time = _time
    o.save()

    redis.zadd(R_UNREAD_MSG_ZSET, _time, o._id)


def msg_unread_list(start=0, stop=-1):
    """ 未读消息的列表.

    注意 id_list的值为文档对象的隐藏_id值
    """
    id_list = redis.zrange(R_UNREAD_MSG_ZSET, start, stop)
    # return [Msg.find_one(id) for id in id_list]
    return []


def msg_unread_count():
    return redis.zcard(R_UNREAD_MSG_ZSET)


def msg_read(_id):
    """ 消息已读. 从未读 hash 表中移除
    """
    redis.zrem(R_UNREAD_MSG_ZSET, _id)


def msg_read_all():
    """ 全部阅读
    """
    redis.delete(R_UNREAD_MSG_ZSET)

if __name__ == '__main__':
    # msg_new('kzing', 'kzin@gmail.com', 'hello, msg')
    # msg_new('kzing', 'kzin@gmail.com', 'hello, msg2222')
    for o in msg_unread_list():
        # o = Msg.find_one(_id)
        print(o.user_name, o.user_mail, o.msg, o._id)
    # print(msg_unread_count())
    # msg_read('543ba0bcf543d635544bb588')
    # print(msg_unread_count())
    # msg_read_all()
    # print(msg_unread_count())
    # print(msg_unread_list())
