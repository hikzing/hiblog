# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413810516.905137
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/blogpage.html'
_template_uri = 'admin/blogpage.html'
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
        this = context.get('this', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n<body>\r\n\r\n    <div id="wrapper">\r\n\r\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n        ')
        __M_writer(unicode(base.nav_side('blog_new')))
        __M_writer(u'\r\n\r\n        <div id="page-wrapper">\r\n            <div class="row">\r\n                <div class="col-lg-12">\r\n')
        if this.get_argument('new', None):
            __M_writer(u'                        <h1 class="page-header">Blog New</h1>\r\n')
        else:
            __M_writer(u'                        <h1 class="page-header">Blog Edit</h1>\r\n')
        __M_writer(u'                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <div class="row">\r\n                <div class="col-lg-20">\r\n                    <div class="panel panel-default">\r\n\r\n                        <div class="panel-body">\r\n                            <div class="row">\r\n                                <div class="col-lg-8 col-centered">\r\n                                    <form role="form" id="blogForm">\r\n                                        <div class="form-group">\r\n                                            <label>\u4f5c\u8005</label>\r\n                                            <input class="form-control" id="author" value="')
        __M_writer(unicode(data.author))
        __M_writer(u'">\r\n                                            <p class="help-block hide">\u4f5c\u8005\u4e0d\u80fd\u4e3a\u7a7a</p>\r\n                                        </div>\r\n\r\n                                        <div class="form-group">\r\n                                            <label>\u6807\u9898</label>\r\n                                            <input class="form-control" value="')
        __M_writer(unicode(data.title))
        __M_writer(u'" id="title">\r\n                                            <p class="help-block hide">\u6807\u9898\u4e0d\u80fd\u4e3a\u7a7a</p>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>\u5185\u5bb9(\u652f\u6301MarkDown)</label>\r\n                                            <textarea class="form-control" rows="12" id="content">')
        __M_writer(unicode(data.content))
        __M_writer(u'</textarea>\r\n                                            <p class="help-block hide">\u5185\u5bb9\u4e0d\u80fd\u4e3a\u7a7a</p>\r\n                                        </div>\r\n                                        <input class="hide" value="')
        __M_writer(unicode(data._id))
        __M_writer(u'" id="blog_id">\r\n')
        if this.get_argument('new', None):
            __M_writer(u'                                        <input type="submit" class="form-control" value="\u65b0\u5efa">\r\n')
        else:
            __M_writer(u'                                        <input type="submit" class="form-control" value="\u4fdd\u5b58">\r\n')
        __M_writer(u'                                     </form>\r\n                                </div>\r\n                                <!-- /.col-lg-6 (nested) -->\r\n                            </div>\r\n                            <!-- /.row (nested) -->\r\n                        </div>\r\n                        <!-- /.panel-body -->\r\n                    </div>\r\n                    <!-- /.panel -->\r\n                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <!-- /.row -->\r\n        </div>\r\n        <!-- /#page-wrapper -->\r\n\r\n    </div>\r\n    <!-- /#wrapper -->\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 1, "25": 0, "33": 1, "34": 3, "35": 3, "36": 8, "37": 8, "38": 10, "39": 10, "40": 15, "41": 16, "42": 17, "43": 18, "44": 20, "45": 33, "46": 33, "47": 39, "48": 39, "49": 44, "50": 44, "51": 47, "52": 47, "53": 48, "54": 49, "55": 50, "56": 51, "57": 53, "58": 72, "59": 72, "65": 59}, "uri": "admin/blogpage.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/blogpage.html"}
__M_END_METADATA
"""
