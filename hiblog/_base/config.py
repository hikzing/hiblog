#!/usr/bin/env python
# coding:utf-8
from _base.double_star import Star


class Config:

    """ 主配置文件
    """
    DEBUG = False

    APP = 'blog'       # mongodb将会以此作为默认的数据库名

    host = 'localhost'   # 你的域名(**必填**)

    ########## 以下内容一般不用修改 ############
    class REDIS(Star):
        host = "127.0.0.1"
        port = 6379
    REDIS = REDIS()

    class MONGO(Star):
        host = "127.0.0.1"
        port = 27017
    MONGO = MONGO()
