#!/usr/bin/env python
from model.db import R, redis
from os import urandom
from base64 import urlsafe_b64decode, urlsafe_b64encode
import binascii
# from _base.config import HOST

R_SESION = R.SESSION('%s')


class Session:

    EXPIRE = 365

    @classmethod
    def new(cls, id, expire=EXPIRE * 24 * 3600):
        id = int(id)
        if id:
            key = R_SESION % id
            s = redis.get(key) or urandom(12)
            redis.setex(key, expire, s)
            return _encode(id, s)

    @classmethod
    def rm(cls, id):
        key = R_SESION % id
        if key:
            redis.delete(key)

    @classmethod
    def id_by_b64(cls, session):
        id, binary = _decode(session)
        if id:
            key = R_SESION % id
            if binary and binary == redis.get(key):
                return id

    def _encode(self, account, session, encode=urlsafe_b64encode):
        return urlsafe_b64encode('{}.{}'.format(account, session))


def _encode(id, session, encode=urlsafe_b64encode):
    return '{id}.{ck_key}'.format(id=id, ck_key=encode(session))


def _decode(session):
    if not session:
        return None, None
    id, value = session.split('.')
    try:
        value = urlsafe_b64decode(value)
    except (binascii.Error, TypeError):
        return None, None
    return int(id), value


def _session_new(self, account, user_id):
    session = Session.new(user_id)
    self.set_cookie('S', session, domain="." + HOST, expires_days=Session.EXPIRE_DAY)
    self.set_cookie('E', account, domain="auth." + HOST, expires_days=Session.EXPIRE_DAY)
