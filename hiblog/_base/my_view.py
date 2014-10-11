#!/usr/bin/env python
# coding: utf-8
import _env
from tornado.web import RequestHandler, HTTPError
from model.session import Session
from _base.mako_render import mako_render


class BaseView(RequestHandler):

    @property
    def current_user(self):
        """ 从 cookie 中获取用户的名字
        """
        if not hasattr(self, '_current_user'):
            cookie = self.get_cookie('auth')
            self._current_user = _id = Session.id_by_b64(cookie)
            if cookie and not _id:
                self.clear_cookie('S', domain='.' + self.request.host)
        return self._current_user_id

    @current_user.setter
    def set_current_user(self, value):
        self._current_user = value

    def render(self, template_name=None, **kwds):
        """ 重写render的行为.
        """
        if not self._finished:
            if template_name is None:
                if not hasattr(self, 'template'):
                    # 若没有提供模板名, 则使用上层所在的modules名加上类名
                    # 如: 在view/admin/index.py 里有一个名为test的 handlers 类
                    # 则其默认模板名为admin/test.html
                    path = self.__module__.split('.')
                    path.pop(0)
                    path.pop(-1)
                    self.template = '{}/{}.html'.format(
                        '/'.join(path),
                        self.__class__.__name__
                    )
                template_name = self.template.lower()

            # 可在前端Mako中直接获取以下定义.
            kwds['current_user'] = self.current_user
            kwds['current_user_id'] = self.current_user_id
            kwds['request'] = self.request
            kwds['this'] = self
            self.finish(mako_render(template_name, **kwds))


class LoginView(BaseView):

    """只接受已登录用户的请求. 否则引导其注册
    """
    _login_templates = 'login.html'

    def prepare(self):
        super(LoginView, self).prepare()
        if not self._finished:
            if not self.current_user_id:
                self.render(self._login_templates)


class AdminView(LoginView):

    """ 网站管理员
    """

    def preapare(self):
        super(AdminView, self).preapare()
        if not self._finished:
            if not self.host.can_admin(self.current_user_id):  # TODO
                raise HTTPError(405)


class JsonView(BaseView):

    """返回的数据为 Json格式

    一般用于前端用 Ajax 获取数据
    """

    def render(self, chunk):
        if not chunk:
            chunk = '{}'
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        super(JsonView, self).finish(chunk)


class JsonLoginView(JsonView):

    def prepare(self):
        if not self.current_user_id:
            raise HTTPError(405)


class JsonAdminView(JsonLoginView):

    def prepare(self):
        super(JsonAdminView, self).prepare()
        if not self._finished:
            if not self.host.can_admin(self.current_user_id):
                raise HTTPError(405)
