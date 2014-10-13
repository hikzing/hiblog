# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413201590.795948
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<html>\n    <head>\n        <link href="../static/css/login.css" rel="stylesheet">\n    </head>\n\n    <body>\n        <main>\n            <h1>Welcom :)</h1>\n            <form class="flp" id="submitForm">\n                <div>\n                    <input type="email" id="email" required>\n                    <label for="email">Email</label>\n                </div>\n                <div>\n                    <input type="password" id="password" required data-validation-required-message="Please enter your email address."/>\n                    <label for="password">Password</label>\n                </div>\n                <input type="submit" value="Login" id="submit" />\n            </form>\n        </main>\n\n        <script src="../static/js/jquery.min.js"></script>\n        <script src="../static/js/jquery.easing.min.js"></script>\n        <script src="../static/js/login.js"></script>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "login.html", "filename": "/web/kzing.net/hiblog/html/templates/login.html"}
__M_END_METADATA
"""
