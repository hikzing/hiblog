#coding:utf-8

import sys
from os.path import abspath, dirname, join

# 方便模块查找, 开发环境的测试
prefix = abspath(join(dirname(__file__), '..'))

if prefix not in sys.path:
    sys.path.append(prefix)
