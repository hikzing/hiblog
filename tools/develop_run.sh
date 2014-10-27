#!/usr/bin/env sh

# just for develop user.
mongod
redis-server
python ./run.py
