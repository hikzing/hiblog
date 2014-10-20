# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413809108.649859
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/index.html'
_template_uri = 'admin/index.html'
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

    ns = runtime.TemplateNamespace(u'pager', context._clean_inheritance_tokens(), templateuri=u'../_pager.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pager')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        blogs = context.get('blogs', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        limit = context.get('limit', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        total = context.get('total', UNDEFINED)
        pager = _mako_get_namespace(context, 'pager')
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        __M_writer(u'\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n<body>\r\n\r\n    <div id="wrapper">\r\n\r\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n        ')
        __M_writer(unicode(base.nav_side()))
        __M_writer(u'\r\n        <div id="page-wrapper">\r\n            <div class="row">\r\n                <div class="col-lg-12">\r\n                    <h1 class="page-header">\u6700\u8fd1\u66f4\u65b0</h1>\r\n                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n                    <!-- /.panel -->\r\n                    <div class="panel panel-default">\r\n\r\n                        <!-- /.panel-heading -->\r\n                        <div class="panel-body">\r\n                            <ul class="timeline">\r\n')
        for index, blog in enumerate(blogs):
            if index & 1:
                __M_writer(u'                                        <li class="timeline-inverted">\r\n')
            else:
                __M_writer(u'                                        <li>\r\n')
            __M_writer(u'                                        <div class="timeline-badge">\r\n                                        <!-- <i classs=></i> -->\r\n                                        <span>')
            __M_writer(unicode(index))
            __M_writer(u'</span>\r\n                                        </div>\r\n                                        <div class="timeline-panel">\r\n                                            <div class="timeline-heading">\r\n                                                <h4 class="timeline-title">')
            __M_writer(unicode(blog.title))
            __M_writer(u'</h4>\r\n                                                <p><small class="text-muted"><i class="fa fa-clock-o"></i> ')
            __M_writer(unicode(blog.post_date))
            __M_writer(u' by ')
            __M_writer(unicode(blog.author))
            __M_writer(u'</small>\r\n                                                </p>\r\n                                            </div>\r\n                                            <div class="timeline-body">\r\n                                                <p>')
            __M_writer(unicode(blog.summarize))
            __M_writer(u'</p>\r\n                                            </div>\r\n                                        <hr>\r\n                                        <div class="btn-group">\r\n                                                <button type="button" class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown">\r\n                                                    <i class="fa fa-gear"></i>  <span class="caret"></span>\r\n                                                </button>\r\n                                                <ul class="dropdown-menu" role="menu">\r\n                                                    <li><a href="/admin/blog/edit?blog_id=')
            __M_writer(unicode(blog._id))
            __M_writer(u'">\u7f16\u8f91</a>\r\n                                                    </li>\r\n                                                    <li><a href="javascript:void(0)" onclick=\'delBlog("')
            __M_writer(unicode(blog._id))
            __M_writer(u'")\' >\u5220\u9664</a>\r\n                                                    </li>\r\n                                                </ul>\r\n                                            </div>\r\n                                        </div>\r\n                                    </li>\r\n')
        __M_writer(u'                        </div>\r\n                        <!-- /.panel-body -->\r\n                    </div>\r\n                    <!-- /.panel -->\r\n                ')
        __M_writer(unicode(pager.Pager(total, limit)))
        __M_writer(u'\r\n                </div>\r\n        </div>\r\n        <!-- /#page-wrapper -->\r\n\r\n    </div>\r\n    <!-- /#wrapper -->\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n</body>\r\n\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 1, "25": 2, "28": 0, "39": 1, "40": 2, "41": 4, "42": 4, "43": 9, "44": 9, "45": 10, "46": 10, "47": 24, "48": 25, "49": 26, "50": 27, "51": 28, "52": 30, "53": 32, "54": 32, "55": 36, "56": 36, "57": 37, "58": 37, "59": 37, "60": 37, "61": 41, "62": 41, "63": 49, "64": 49, "65": 51, "66": 51, "67": 58, "68": 62, "69": 62, "70": 70, "71": 70, "77": 71}, "uri": "admin/index.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/index.html"}
__M_END_METADATA
"""
