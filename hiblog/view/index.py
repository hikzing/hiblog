#!/usr/bin/env python
# coding:utf-8
import _env
from _base.app import Route
from _base.my_view import BaseView
from _base.config import Config, Prepare
from _base.json_ob import JsOb
from model.blog import blog_lists_by_date, blog_from_slug_name, blog_count
from model.my_markdown import turn_to_markdown


route = Route()


@route('/')
class Index(BaseView):

    blog_limit = 8  # 主页展示的文章数量

    def get(self):
        offset = int(self.get_argument('p', 1)) - 1
        limit = self.blog_limit

        blogs = []
        for ob in blog_lists_by_date(offset * limit, limit):
            blogs.append(JsOb(
                title=ob.title,
                summarize=turn_to_markdown(ob.summarize),
                author=ob.author,
                post_date=ob.post_date,
                author_page=ob.author_page or 'about',  # 文章作者默认为网站拥有者
                slug_title=ob.slug_title,
            ))
        return self.render(
            home_title=Prepare.name,  # 主页的标题
            home_desc=Prepare.desc,   # 主页描述
            blogs=blogs,
            total=blog_count(),           # 分页用: blog的总数.
            limit=limit                   # 分页用: 每页的显示数.
        )


@route('/blog/(.+)')
class Post(BaseView):

    def get(self, blog_name):

        blog = blog_from_slug_name(blog_name)
        if blog:
            return self.render(
                title='{} | article'.format(Config.host),
                blog_title=blog.title,
                author=blog.author,
                post_date=blog.post_date,
                content=turn_to_markdown(blog.content),
                author_page=blog.author_page,
            )
        else:
            return self.write('404')  # TODO


@route('/about')
class About(BaseView):

    def get(self):
        return self.render(
            title=Prepare.about_title,
            # TODO
        )


@route('/about/me')
class Resume(BaseView):

    def get(self):
        return self.render()


@route('/contact')
class Contact(BaseView):

    def get(self):
        return self.render(
            contact_title=Prepare.contact_title,
            contact_desc=Prepare.contact_desc,
            contact_msg=Prepare.contact_msg
        )

# @route('/category')
# class Category(BaseView):

#     def get(self):
#         self.render()


# @route('/tag')
# class Tag(BaseView):

#     def get(self):
#         self.render()



# if __name__ == '__main__':
#     app.run()
