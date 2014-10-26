# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414308503.736796
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/index.html'
_template_uri = '/index.html'
_source_encoding = 'utf-8'
_exports = []



from _base.setting import HOME_TITLE, HOME_DESC


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'_base.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    ns = runtime.TemplateNamespace(u'pager', context._clean_inheritance_tokens(), templateuri=u'_pager.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pager')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pager = _mako_get_namespace(context, 'pager')
        blogs = context.get('blogs', UNDEFINED)
        total = context.get('total', UNDEFINED)
        limit = context.get('limit', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        __M_writer(u'\r\n')
        __M_writer(u'\r\n\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n\r\n<body>\r\n\r\n    <!-- Navigation -->\r\n    ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n    <header class="intro-header" style="background-image: url(\'../static/img/home-bg.jpg\')">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                    <div class="site-heading">\r\n                        <h1>')
        __M_writer(unicode(HOME_TITLE))
        __M_writer(u'</h1>\r\n                        <hr class="small">\r\n                        <span class="subheading">')
        __M_writer(unicode(HOME_DESC))
        __M_writer(u'</span>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </header>\r\n\r\n    <!-- Main Content -->\r\n    <div class="container">\r\n        <div class="row">\r\n            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n')
        if not blogs:
            __M_writer(u'                    <div class="post-preview">\r\n                        <h2 class="post-subtitle">\u8fd8\u6ca1\u6709\u5199\u8fc7blog. \u53bb\u540e\u53f0\u65b0\u5efa\u4e00\u7bc7\u5427: )</h2>\r\n')
        else:
            for blog in blogs:
                __M_writer(u'                    <div class="post-preview">\r\n                        <a href="/blog/')
                __M_writer(unicode(blog.slug_title))
                __M_writer(u'">\r\n                            <h2 class="post-title">\r\n                                ')
                __M_writer(unicode(blog.title))
                __M_writer(u'\r\n                            </h2>\r\n                            <h3 class="post-subtitle">\r\n                                ')
                __M_writer(unicode(blog.summarize))
                __M_writer(u'\r\n                            </h3>\r\n                        </a>\r\n                        <p class="post-meta">Posted by <a href="')
                __M_writer(unicode(blog.author_page))
                __M_writer(u'">')
                __M_writer(unicode(blog.author))
                __M_writer(u'</a> on ')
                __M_writer(unicode(blog.post_date))
                __M_writer(u'</p>\r\n                    </div>\r\n                    <hr>\r\n')
        __M_writer(u'                <!-- Pager -->\r\n                ')
        __M_writer(unicode(pager.Pager(total, limit)))
        __M_writer(u'\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n    <hr>\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "26": 4, "29": 5, "32": 0, "42": 3, "43": 4, "44": 5, "45": 8, "46": 8, "47": 13, "48": 13, "49": 20, "50": 20, "51": 22, "52": 22, "53": 33, "54": 34, "55": 36, "56": 37, "57": 38, "58": 39, "59": 39, "60": 41, "61": 41, "62": 44, "63": 44, "64": 47, "65": 47, "66": 47, "67": 47, "68": 47, "69": 47, "70": 52, "71": 53, "72": 53, "73": 60, "74": 60, "80": 74}, "uri": "/index.html", "filename": "/web/kzing.net/hiblog/html/templates/index.html"}
__M_END_METADATA
"""
