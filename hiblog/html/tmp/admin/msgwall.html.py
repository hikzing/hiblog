# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414309513.981951
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/admin/msgwall.html'
_template_uri = 'admin/msgwall.html'
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
        msgs = context.get('msgs', UNDEFINED)
        base = _mako_get_namespace(context, 'base')
        limit = context.get('limit', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        total = context.get('total', UNDEFINED)
        pager = _mako_get_namespace(context, 'pager')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\n\n<body>\n    <div id="wrapper">\n\n        ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\n        ')
        __M_writer(unicode(base.nav_side('msg')))
        __M_writer(u'\n        <div id="page-wrapper">\n            <div class="row">\n                <div class="col-lg-12">\n                    <h1 class="page-header">\u7559\u8a00\u5899</h1>\n                </div>\n            </div>\n\n            <!-- /.row -->\n\n')
        for index, msg in enumerate(msgs):
            if not index & 1:
                __M_writer(u'                    <div class="row">\n')
            __M_writer(u'                <div class="col-lg-6">\n')
            if msg.has_read:
                __M_writer(u'                        <div class="panel panel-default">\n')
            else:
                __M_writer(u'                        <div class="panel panel-green">\n')
            __M_writer(u'                        <div class="panel-heading">\n                            <b>From: ')
            __M_writer(unicode(msg.user_name))
            __M_writer(u'\n                            </b>\n                        </div>\n                        <div class="panel-body" onclick="window.location.href=\'/admin/msg_wall/')
            __M_writer(unicode(msg._id))
            __M_writer(u'\'">\n                            <p>')
            __M_writer(unicode(msg.content))
            __M_writer(u'</p>\n                        </div>\n                        <div class="panel-footer">\n                            Email: <b>')
            __M_writer(unicode(msg.user_mail))
            __M_writer(u'</b> Post on <b>')
            __M_writer(unicode(msg.post_time))
            __M_writer(u'</b>\n                        </div>\n                    </div>\n                </div>\n')
            if index & 1:
                __M_writer(u'                    </div>\n')
        __M_writer(u'            <div class="row">\n                <div class="col-lg-6">\n                    <div class="panel panel-green">\n                        <div class="panel-heading">\n                            From: <b>Kzing</b>\n                        </div>\n                        <div class="panel-body">\n                            <p>\u6b22\u8fce\u4f7f\u7528 HiBlog</p>\n                            <p>\u5982\u679c\u4f60\u9047\u5230\u4ec0\u4e48\u95ee\u9898, \u53ef\u4ee5\u901a\u8fc7\u4e0b\u9762\u7684\u65b9\u5f0f\u8054\u7cfb\u6211</p>\n                            <p><b>kzinglzy@gmail.com</b> | <a href="https://github.com/Kzinglzy/hiblog">Github</a></p>\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n        </div>\n        ')
        __M_writer(unicode(pager.Pager(total, limit)))
        __M_writer(u'\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 1, "25": 2, "28": 0, "39": 1, "40": 2, "41": 4, "42": 4, "43": 9, "44": 9, "45": 10, "46": 10, "47": 20, "48": 21, "49": 22, "50": 24, "51": 25, "52": 26, "53": 27, "54": 28, "55": 30, "56": 31, "57": 31, "58": 34, "59": 34, "60": 35, "61": 35, "62": 38, "63": 38, "64": 38, "65": 38, "66": 42, "67": 43, "68": 46, "69": 62, "70": 62, "71": 63, "72": 63, "78": 72}, "uri": "admin/msgwall.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/msgwall.html"}
__M_END_METADATA
"""
