# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414308573.121979
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/post.html'
_template_uri = '/post.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'_base.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content = context.get('content', UNDEFINED)
        author = context.get('author', UNDEFINED)
        author_page = context.get('author_page', UNDEFINED)
        post_date = context.get('post_date', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n\r\n<body>\r\n\r\n    ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n    <!-- Page Header -->\r\n    <!-- Set your background image for this header on the line below. -->\r\n    <header class="intro-header" style="background-image: url(\'../static/img/post-bg.jpg\')">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                    <div class="post-heading">\r\n                        <h1>')
        __M_writer(unicode(blog_title))
        __M_writer(u'</h1>\r\n                        <!-- <h2 class="subheading">Problems look mighty small from 150 miles up</h2> -->\r\n                        <span class="meta">Posted by <a href="')
        __M_writer(unicode(author_page))
        __M_writer(u'">')
        __M_writer(unicode(author))
        __M_writer(u'</a> on ')
        __M_writer(unicode(post_date))
        __M_writer(u'</span>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </header>\r\n\r\n    <!-- Post Content -->\r\n    <article>\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                ')
        __M_writer(unicode(content))
        __M_writer(u'\r\n                ')
        __M_writer(unicode(base.disqus()))
        __M_writer(u'\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </article>\r\n\r\n    <hr>\r\n\r\n\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 1, "25": 0, "36": 1, "37": 3, "38": 3, "39": 7, "40": 7, "41": 16, "42": 16, "43": 18, "44": 18, "45": 18, "46": 18, "47": 18, "48": 18, "49": 30, "50": 30, "51": 31, "52": 31, "53": 41, "54": 41, "60": 54}, "uri": "/post.html", "filename": "/web/kzing.net/hiblog/html/templates/post.html"}
__M_END_METADATA
"""
