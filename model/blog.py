#!/usr/bin/env python
# coding:utf-8
import time
from model.db import Doc


class Blog(Doc):

    structure = dict(
        author=basestring,      # 作者
        title=basestring,       # 标题
        content=basestring,     # 正文
        category=basestring,    # 分类
        tags=[basestring],      # 标签
        _date=float,            # 发布日期
        watch=int,              # 查看数
        author_page=basestring,  # 作者主页
    )

    default_values = dict(
        _date=time.time(),      # 默认为当前时间的时间戳
        watch=1
    )

    indexs = [{
        'fileds': 'title',
        'unique': True
    }]

    @property
    def slug_title(self):
        """url友好型值
        """
        return '-'.join(self.title.split())

    @property
    def post_date(self, style="%Y-%m-%d"):
        return time.strftime(style, time.localtime(self._date))

    @property
    def summarize(self):
        """摘要
        """
        return self.content.split('\n', 1)[0]  # TODO: may be there is a better


def blog_lists_by_date(offset=0, limit=0):
    """按日期先后返回博客列表
    """
    return Blog.find(limit=limit, skip=offset, sort=[('_date', 1)])


def blog_from_slug_name(slug):
    """从指定的 slug name 获取对应的 blog
    """
    return Blog.find_one(dict(title=slug.replace('-', ' ')))


def blog_count(*args, **kwds):
    """blog的数量. 参数为空时返回全部 blog 的数量.
    """
    return Blog.count(*args, **kwds)

# def blog_lists_by_category(category, offset=0, limit=0):
#     """返回指定分类下的所有博客的列表
#     """
#     return Blog.find({'category': category},
#                      limit=limit,
#                      skip=offset,
#                      sort=[('_date', 1)]
#                      )

# def watch_new(blog):
#     """更新blog被查看的次数
#     """
#     return Blog.update({'title': blog}, {'$inc': {'watch': 1}})


if __name__ == '__main__':
    print(blog_count())
