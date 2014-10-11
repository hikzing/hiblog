#!/usr/bin/env python
# coding: utf-8
import _env

from _base.config import Config
from _base.mako_render import mako_render
from model.session import Session
from tornado.web import RequestHandler, HTTPError
from _base.json_ob import StripJsOb
from yajl import loads


class BaseView(RequestHandler):

    def get_current_user(self):
        """重写此方法以从 cookie 中获取用户身份
        """
        cookie = self.get_cookie('auth')
        self._current_user = _account = Session.account_by_cookie(cookie)
        if cookie and not _account:
            self.clear_cookie('auth', domain='.' + self.request.host)
        return self._current_user

    def set_session(self, account):
        self.set_cookie(
            'auth',
            Session.new(account),
            domain='.' + Config.HOST,
            expires_days=Session.EXPIRE_DAY
        )

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
            if not self.current_user:
                self.render(self._login_templates)


class AdminView(LoginView):

    """ 网站管理员
    """

    def preapare(self):
        super(AdminView, self).preapare()
        if not self._finished:
            if not self.current_user in Config.admin_set:
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
        if not self.current_user:
            raise HTTPError(405)


class JsonAdminView(JsonLoginView):

    def prepare(self):
        super(JsonAdminView, self).prepare()
        if not self._finished:
            if not self.host.can_admin(self.current_user):
                raise HTTPError(405)


class JsonErrView(JsonView):

    @property
    def json(self):
        return StripJsOb(**loads(self.request.body))

    def render(self, chunk):
        if chunk:
            chunk = '{"err":%s}' % chunk  # 前端通过获取键为err的json对象来进行对应的错误处理
        else:
            chunk = '{}'
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.finish(chunk)

    def get(self):
        """URL 转换, 将 HTTP 方式从 GET 转为 POST
        """
        o = self.get_argument('o')
        self.request.body = o
        self.post()

    def finish(self, chunk={}):
        callback = self.get_argument('callback', None)
        if callback:
            chunk = "%s(%s)" % (callback, chunk)
        # self.finish(chunk)
        super(JsonErrView, self).finish(chunk)
