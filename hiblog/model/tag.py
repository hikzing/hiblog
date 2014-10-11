#!/usr/bin/env python
# coding:utf-8
import _env
from model.db import Doc


class Tag(Doc):

    structure = dict(
        name=basestring,    # 标签名
        blog=[basestring],  # 博客列表
        blog_count=int,     # blog数量
    )

    # require_fileds = ['blog_count']  # TODO

    default_values = dict(
        blog_count=0
    )


def tag_lists_by_count(offset=0, limit=0):
    """按包含的blog数量大小返回对应的 tag 列表
    """
    return Tag.find(limit=limit,
                    offset=offset,
                    sort=[('blog_count', 1)]
                    )


def tag_update_by_blog(tags, blog):
    """更新一篇blog下对应的所有tags
    """
    for tag in tags:
        _tag = Tag.find_one({'name': tag})
        if _tag:
            blog_list = _tag.blog
            if blog not in blog_list:
                blog_list.append(blog)  # TODO
                _tag.blog_count += 1
            _tag.save()
        else:
            Tag({'blog': [blog]}, True).upsert({'name': tag})


if __name__ == '__main__':
    # print(Tag.find())
    # tag_update_by_blog(['a', 'b', 'c'], 'blog')
    # tag_update_by_blog(['a', 'd'], 'blog2')
    # tag_update_by_blog(['a', 'e', 'f'], 'blog3')

    # for each in Tag.find():
    #     print each.name, each.blog, each.blog_count
    # Tag.remove()
    pass
