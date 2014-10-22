# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413968384.292228
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/msginfo.html'
_template_uri = 'admin/msginfo.html'
_source_encoding = 'utf-8'
_exports = []



from model.my_markdown import turn_to_markdown


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
        msg = context.get('msg', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\n\n<body>\n    <div id="wrapper">\n\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\n        ')
        __M_writer(unicode(base.nav_side('msg')))
        __M_writer(u'\n        <div id="page-wrapper">\n            <div class="row">\n                <div class="col-lg-12">\n                    <h2 class="page-header text-center">\n                        <b>')
        __M_writer(unicode(msg.user_mail))
        __M_writer(u'</b> post on <b>')
        __M_writer(unicode(msg.post_time))
        __M_writer(u'</b>\n                    </h2>\n                </div>\n                <!-- /.col-lg-12 -->\n            </div>\n            <!-- /.row -->\n\n            <div class="row">\n                <div class="col-md-10 col-md-offset-1">\n                        <div class="jumbotron">\n                            <h2>')
        __M_writer(unicode(msg.user_name))
        __M_writer(u'</h2>\n                            <hr>\n                            <p>')
        __M_writer(unicode(turn_to_markdown(msg.content)))
        __M_writer(u'</p>\n                        </div>\n                        <p class="text-center">\n                            <a class="btn btn-info" role="button" onclick=\'MsgAction("')
        __M_writer(unicode(msg._id))
        __M_writer(u'", "READ")\'>\n                                Read\n                                <i class="fa fa-check"></i>\n                            </a>\n                            <a class="btn btn-danger    " role="button" onclick=\'MsgAction("')
        __M_writer(unicode(msg._id))
        __M_writer(u'", "DEL")\'>\n                                Delete\n                                <i class="fa fa-times"></i>\n                            </a>\n                        </p>\n                </div>\n            </div>\n    </div>\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "26": 4, "29": 0, "36": 3, "37": 4, "38": 6, "39": 6, "40": 11, "41": 11, "42": 12, "43": 12, "44": 17, "45": 17, "46": 17, "47": 17, "48": 27, "49": 27, "50": 29, "51": 29, "52": 32, "53": 32, "54": 36, "55": 36, "56": 44, "57": 44, "63": 57}, "uri": "admin/msginfo.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/msginfo.html"}
__M_END_METADATA
"""
