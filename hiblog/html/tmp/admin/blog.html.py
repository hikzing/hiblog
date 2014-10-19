# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413636593.291627
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/blog.html'
_template_uri = 'admin/blog.html'
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
        __M_writer(u'                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <div class="row">\r\n                <div class="col-lg-20">\r\n                    <div class="panel panel-default">\r\n\r\n                        <div class="panel-body">\r\n                            <div class="row">\r\n                                <div class="col-lg-8 col-centered">\r\n                                    <form role="form">\r\n                                        <div class="form-group">\r\n                                            <label>Text Input</label>\r\n                                            <input class="form-control">\r\n                                            <p class="help-block">Example block-level help text here.</p>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Text Input with Placeholder</label>\r\n                                            <input class="form-control" placeholder="Enter text">\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Static Control</label>\r\n                                            <p class="form-control-static">email@example.com</p>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>File input</label>\r\n                                            <input type="file">\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Text area</label>\r\n                                            <textarea class="form-control" rows="3"></textarea>\r\n                                        </div>\r\n                                     </form>\r\n                                </div>\r\n                                <!-- /.col-lg-6 (nested) -->\r\n                            </div>\r\n                            <!-- /.row (nested) -->\r\n                        </div>\r\n                        <!-- /.panel-body -->\r\n                    </div>\r\n                    <!-- /.panel -->\r\n                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <!-- /.row -->\r\n        </div>\r\n        <!-- /#page-wrapper -->\r\n\r\n    </div>\r\n    <!-- /#wrapper -->\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "33": 3, "34": 3, "35": 8, "36": 8, "37": 10, "38": 10, "39": 15, "40": 16, "41": 17, "42": 18, "43": 20, "44": 71, "45": 71, "51": 45, "22": 1, "25": 0}, "uri": "admin/blog.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/blog.html"}
__M_END_METADATA
"""
