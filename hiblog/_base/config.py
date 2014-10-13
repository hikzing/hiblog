#!/usr/bin/env python
# coding:utf-8
from _base.double_star import Star


class Config:

    """ 主配置文件
    """

    # app
    APP = 'blog'
    DEBUG = True

    host = 'localhost:8888'

    # redis
    class REDIS(Star):
        host = "127.0.0.1"
        port = 6379
    REDIS = REDIS()

    # mongo
    class MONGO(Star):
        host = "127.0.0.1"
        port = 27017
    MONGO = MONGO()

    # admin
    admin_set = {'kzing@gmail.com', }


class Prepare:

    # index page
    name = "Hi, Blog"
    desc = 'A Clean Blog System'

    # contact
    contact_title = 'Contact Me'
    contact_desc = 'Have questions? I have answers (maybe).'
    contact_msg = """Want to get in touch with me?
                    Fill out the form below to send me a message
                    and I will try to get back to you within 24 hours!
                    """

    # about
    about_title = 'About me'
