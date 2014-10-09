#!/usr/bin/env python
# coding:utf-8
from _base.double_star import Star


class Config:

    """配置文件

    使用:
        >>> from config import Config
        >>> db.connection(**Config.REDIS)
    """

    host_name = "hiblog"
    host_desc = 'a clean blog system'

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
