# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412069262.83208
_enable_loop = True
_template_filename = '/web/kzing.net/html/templates/index.html'
_template_uri = 'index.html'
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
        home_desc = context.get('home_desc', UNDEFINED)
        home_title = context.get('home_title', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        limit = context.get('limit', UNDEFINED)
        total = context.get('total', UNDEFINED)
        blogs = context.get('blogs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        __M_writer(u'\r\n\r\n\r\n')
        __M_writer(unicode(base.head('kzing.net | Home')))
        __M_writer(u'\r\n\r\n<body>\r\n\r\n    <!-- Navigation -->\r\n    ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n    <header class="intro-header" style="background-image: url(\'../static/img/home-bg.jpg\')">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                    <div class="site-heading">\r\n                        <h1>')
        __M_writer(unicode(home_title))
        __M_writer(u'</h1>\r\n                        <hr class="small">\r\n                        <span class="subheading">')
        __M_writer(unicode(home_desc))
        __M_writer(u'</span>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </header>\r\n\r\n    <!-- Main Content -->\r\n    <div class="container">\r\n        <div class="row">\r\n            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n')
        for blog in blogs:
            __M_writer(u'                <div class="post-preview">\r\n                    <a href="/blog/')
            __M_writer(unicode(blog.slug_title))
            __M_writer(u'">\r\n                        <h2 class="post-title">\r\n                            ')
            __M_writer(unicode(blog.title))
            __M_writer(u'\r\n                        </h2>\r\n                        <h3 class="post-subtitle">\r\n                            ')
            __M_writer(unicode(blog.summarize))
            __M_writer(u'\r\n                        </h3>\r\n                    </a>\r\n                    <p class="post-meta">Posted by <a href="')
            __M_writer(unicode(blog.author_page))
            __M_writer(u'">')
            __M_writer(unicode(blog.author))
            __M_writer(u'</a> on ')
            __M_writer(unicode(blog.post_date))
            __M_writer(u'</p>\r\n                </div>\r\n                <hr>\r\n')
        __M_writer(u'\r\n                <!-- Pager -->\r\n                ')
        __M_writer(unicode(base.Pager(total, limit)))
        __M_writer(u'\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n    <hr>\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 2, "25": 0, "36": 1, "37": 2, "38": 5, "39": 5, "40": 10, "41": 10, "42": 17, "43": 17, "44": 19, "45": 19, "46": 30, "47": 31, "48": 32, "49": 32, "50": 34, "51": 34, "52": 37, "53": 37, "54": 40, "55": 40, "56": 40, "57": 40, "58": 40, "59": 40, "60": 44, "61": 46, "62": 46, "63": 53, "64": 53, "70": 64}, "uri": "index.html", "filename": "/web/kzing.net/html/templates/index.html"}
__M_END_METADATA
"""
