#!/usr/bin/env python
import _env

from model.db import R, redis

R_ADMIN_SET = R.ADMIN_SET()


def admin_new(account):
    return redis.sadd(R_ADMIN_SET, account)


def is_admin(mail):
    return redis.sismember(R_ADMIN_SET, mail)
