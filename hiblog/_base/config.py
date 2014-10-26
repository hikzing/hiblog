#!/usr/bin/env python
# coding:utf-8
from _base.double_star import Star


class Config:

    """ 主配置文件
    """
    DEBUG = False

    APP = 'blog'         # mongo将会以此作为默认的数据库名

    host = 'localhost'   # 域名

    ######################

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
