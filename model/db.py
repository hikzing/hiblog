#!/usr/bin/env python
from _base.redis_key import RedisKey
from _base.config import Config
from _base.mongo import Doc as _Doc
import redis as _redis

## redis
redis = _redis.StrictRedis(**Config.REDIS)
R = RedisKey(redis)


## mongo
Doc = _Doc
