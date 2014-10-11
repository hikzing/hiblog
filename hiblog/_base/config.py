#!/usr/bin/env python
# coding:utf-8
from _base.double_star import Star


class Config:

    """ 配置文件
    """

    # host
    host = 'localhost:8888'
    host_name = "hiblog"
    host_desc = 'a clean blog system'

    # app
    APP = 'blog'
    DEBUG = True

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
