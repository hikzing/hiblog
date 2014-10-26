#!/usr/bin/env python
#coding:utf-8

import _env

from os import urandom
from base64 import urlsafe_b64decode, urlsafe_b64encode
from model.db import R, redis
import binascii

R_SESION = R.SESSION('%s')


class Session:

    EXPIRE_DAY = 365

    @classmethod
    def new(cls, account, expire=EXPIRE_DAY * 24 * 3660):
        if account:
            key = R_SESION % account
            s = redis.get(key) or urandom(12)
            redis.setex(key, expire, s)
            return _encode(account, s)

    @classmethod
    def rm(cls, id):
        key = R_SESION % id
        if key:
            redis.delete(key)

    @classmethod
    def account_by_cookie(cls, cookie):
        account, binary = _decode(cookie)
        if account:
            key = R_SESION % account
            if binary and binary == redis.get(key):
                return account


def _decode(session):
    if not session:
        return None, None
    try:
        account_value = urlsafe_b64decode(session)
    except (binascii.Error, TypeError):
        return None, None
    return account_value.split('-', 1)  # (account, session_value)


def _encode(account, session, encode=urlsafe_b64encode):
    return urlsafe_b64encode('{}-{}'.format(account, session))


if __name__ == '__main__':
    pass
