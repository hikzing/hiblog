#!/usr/bin/env python
# coding:utf-8
from _base.int_str import int_str


_EXIST = set()

REDIS_KEY = 'RedisKey'
REDIS_KEY_ID = 'RedisKeyId'


class RedisKey:

    """ 生成更短的redis key 以减少内存使用

    >>> from redis_key import redis, R
    >>> R_NAME = R.NAME('%s')
    >>> redis.set(R_NAME % 'lzy', 'coder')
    """

    def __init__(self, redis):
        self.redis = redis

    def __getattr__(self, attr):

        return lambda name='': self(attr, name)

    def __call__(self, attr, name):
        redis = self.redis
        key = attr + name
        if key in _EXIST:
            raise Exception('redis key has defined: %s' % key)
        _EXIST.add(key)
        if redis:
            k = redis.hget(REDIS_KEY, key)
            if k is None:
                id = redis.incr(REDIS_KEY_ID)
                k = int_str.encode(id)
                if name and '%' in name:
                    k += "'" + name
                redis.hsetnx(REDIS_KEY, key, k)

            return k
