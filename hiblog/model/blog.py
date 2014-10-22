#!/usr/bin/env python
# coding:utf-8
import _env
import time
from model.db import Doc
from _base.json_ob import JsOb
from model.my_markdown import turn_to_markdown
from bson.objectid import ObjectId


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
        """返回时间戳对应的格式化日期值
        """
        now = time.time()
        today = (now // 86400) * 86400
        tomorow = today + 86400
        date = self._date

        if date is None:
            return ''
        elif today < date < tomorow:
            recently = now - date
            if 0 < recently < 3600:  # 发布时间在一小时内
                return 'just now'
            else:
                return '%s hours ago' % (int((recently) // 3600))  # 发布时间在24小时内
        else:
            return time.strftime(style, time.localtime(date))

    @property
    def summarize(self):
        """摘要

        TODO: may be there is a better way : )
        """
        return self.content.split('\n', 1)[0]

    @property
    def detail_dumps(self):
        """生成并返回包含Blog信息的JSON对象
        """
        return JsOb(
            title=self.title,
            summarize=turn_to_markdown(self.summarize),
            author=self.author,
            post_date=self.post_date,
            author_page=self.author_page or 'javascript:void(0)',
            slug_title=self.slug_title,
            tag=self.tags,
            category=self.category,
            _id=self._id,
            watch=self.watch or 0
        )


def blog_lists(offset=0, limit=0):
    """按日期先后返回博客的对象列表
    """
    return Blog.find(limit=limit, skip=offset, sort=[('_date', -1)])


def blog_by_slug_name(slug):
    """从指定的 slug name 获取对应的 blog
    """
    return Blog.find_one(dict(title=slug.replace('-', ' ')))


def blog_count(*args, **kwds):
    """blog的数量. 参数为空时返回全部 blog 的数量.
    """
    return Blog.count(*args, **kwds)


def blog_lists_by_category(category, offset=0, limit=0):
    """返回指定分类下的所有博客的列表
    """
    return Blog.find({'category': category},
                     limit=limit,
                     skip=offset,
                     sort=[('_date', 1)]
                     )


def watch_new(blog):
    """更新blog被查看的次数
    """
    return Blog.update({'title': blog}, {'$inc': {'watch': 1}})


if __name__ == '__main__':
    Blog(dict(author='lzy')).upsert("5444c662f543d637491e7258")
    # print(Blog.find_one("5444c662f543d637491e7258").title.encode('utf-8'))
    # print(Blog.find_one(dict(title="我是一个从后台管理页面创建的长标题哦"))._id)
    # print(isinstance({'_id': "5444c662f543d637491e7258"}, basestring))
    pass
