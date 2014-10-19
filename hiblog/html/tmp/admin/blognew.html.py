# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413634900.934324
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/blognew.html'
_template_uri = 'admin/blognew.html'
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
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n<body>\r\n\r\n    <div id="wrapper">\r\n\r\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n        ')
        __M_writer(unicode(base.nav_side('blog_new')))
        __M_writer(u'\r\n\r\n        <div id="page-wrapper">\r\n            <div class="row">\r\n                <div class="col-lg-12">\r\n                    <h1 class="page-header">Blog New</h1>\r\n                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <div class="row">\r\n                <div class="col-lg-20">\r\n                    <div class="panel panel-default">\r\n\r\n                        <div class="panel-body">\r\n                            <div class="row">\r\n                                <div class="col-lg-8 col-centered">\r\n                                    <form role="form">\r\n                                        <div class="form-group">\r\n                                            <label>Text Input</label>\r\n                                            <input class="form-control">\r\n                                            <p class="help-block">Example block-level help text here.</p>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Text Input with Placeholder</label>\r\n                                            <input class="form-control" placeholder="Enter text">\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Static Control</label>\r\n                                            <p class="form-control-static">email@example.com</p>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>File input</label>\r\n                                            <input type="file">\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                            <label>Text area</label>\r\n                                            <textarea class="form-control" rows="3"></textarea>\r\n                                        </div>\r\n                                     </form>\r\n                                </div>\r\n                                <!-- /.col-lg-6 (nested) -->\r\n                            </div>\r\n                            <!-- /.row (nested) -->\r\n                        </div>\r\n                        <!-- /.panel-body -->\r\n                    </div>\r\n                    <!-- /.panel -->\r\n                </div>\r\n                <!-- /.col-lg-12 -->\r\n            </div>\r\n            <!-- /.row -->\r\n        </div>\r\n        <!-- /#page-wrapper -->\r\n\r\n    </div>\r\n    <!-- /#wrapper -->\r\n\r\n    <!-- jQuery Version 1.11.0 -->\r\n    <script src="js/jquery-1.11.0.js"></script>\r\n\r\n    <!-- Bootstrap Core JavaScript -->\r\n    <script src="js/bootstrap.min.js"></script>\r\n\r\n    <!-- Metis Menu Plugin JavaScript -->\r\n    <script src="js/plugins/metisMenu/metisMenu.min.js"></script>\r\n\r\n    <!-- Morris Charts JavaScript -->\r\n    <script src="js/plugins/morris/raphael.min.js"></script>\r\n    <script src="js/plugins/morris/morris.min.js"></script>\r\n    <script src="js/plugins/morris/morris-data.js"></script>\r\n\r\n    <!-- Custom Theme JavaScript -->\r\n    <script src="js/sb-admin-2.js"></script>\r\n\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 3, "33": 3, "34": 8, "35": 8, "36": 10, "37": 10, "43": 37, "22": 1, "25": 0, "31": 1}, "uri": "admin/blognew.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/blognew.html"}
__M_END_METADATA
"""
