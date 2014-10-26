#coding:utf-8

import sys
from os.path import abspath, dirname, join

# 解决没有设置当前模块路径到sys.path时找不到 module问题

PREFIX = abspath(join(dirname(__file__), '..'))

if PREFIX not in sys.path:
    sys.path.append(PREFIX)
