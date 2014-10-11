#!/usr/bin/env python
# coding:utf-8
import _env
from model.db import Doc


class Category(Doc):

    structure = dict(
        name=basestring,         # 归类名
        description=basestring,  # 描述
        blog=[basestring],       # blog列表
        logo=str,                # 归类的logo名
    )

    @property
    def logo_url(self):
        pass  # TODO


def get_category_lists(self, offset=0, limit=0):
    """获取所有的分类列表
    """
    return Category.find(limit=limit, skip=offset)
