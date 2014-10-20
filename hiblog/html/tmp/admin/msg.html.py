# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413802926.697873
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/msg.html'
_template_uri = 'admin/msg.html'
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
        base = _mako_get_namespace(context, 'base')
        msgs = context.get('msgs', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\n\n<body>\n    <div id="wrapper">\n\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\n        ')
        __M_writer(unicode(base.nav_side()))
        __M_writer(u'\n        <div id="page-wrapper">\n            <div class="row">\n                <div class="col-lg-12">\n                    <h1 class="page-header">\u7559\u8a00\u5899</h1>\n                </div>\n                <!-- /.col-lg-12 -->\n            </div>\n            <!-- /.row -->\n')
        for index, msg in enumerate(msgs):
            if not index & 1:
                __M_writer(u'                    <div class="row">\n')
            __M_writer(u'                <div class="col-lg-6">\n')
            if msg.has_read:
                __M_writer(u'                        <div class="panel panel-default">\n')
            else:
                __M_writer(u'                        <div class="panel panel-green">\n')
            __M_writer(u'                        <div class="panel-heading">\n                            <b>')
            __M_writer(unicode(msg.user_name))
            __M_writer(u'</b>\n                        </div>\n                        <div class="panel-body">\n                            <p>')
            __M_writer(unicode(msg.content))
            __M_writer(u'</p>\n                        </div>\n                        <div class="panel-footer">\n                            Email: <b>')
            __M_writer(unicode(msg.user_mail))
            __M_writer(u'</b> Post on <b>')
            __M_writer(unicode(msg.post_time))
            __M_writer(u'</b>\n                        </div>\n                    </div>\n                </div>\n')
            if index & 1:
                __M_writer(u'                    </div>\n')
        __M_writer(u'        </div>\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 1, "25": 2, "28": 0, "36": 1, "37": 2, "38": 4, "39": 4, "40": 9, "41": 9, "42": 10, "43": 10, "44": 19, "45": 20, "46": 21, "47": 23, "48": 24, "49": 25, "50": 26, "51": 27, "52": 29, "53": 30, "54": 30, "55": 33, "56": 33, "57": 36, "58": 36, "59": 36, "60": 36, "61": 40, "62": 41, "63": 44, "64": 45, "65": 45, "71": 65}, "uri": "admin/msg.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/msg.html"}
__M_END_METADATA
"""
