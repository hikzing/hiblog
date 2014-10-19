# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413636578.84267
_enable_loop = True
_template_filename = u'/web/kzing.net/hiblog/html/templates/_pager.html'
_template_uri = u'/_pager.html'
_source_encoding = 'utf-8'
_exports = ['Pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!-- \u5206\u9875\u5668 -->\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Pager(context,total,limit):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        this = context.get('this', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')

        template = '?p=%s'
        
        now = int(this.get_argument("p", 1))
        _next = _pre = ''
        
        if now * limit < total:
            _next = template % (now + 1)
        
        if now > 1:
            _pre = template % (now - 1)
        
            
        
        __M_writer(u'\n    <ul class="pager">\n')
        if _next:
            __M_writer(u'            <li class="next">\n                <a href="')
            __M_writer(unicode(_next))
            __M_writer(u'">\u4e0b\u4e00\u9875 &rarr;</a>\n            </li>\n')
        if _pre:
            __M_writer(u'            <li class="next pre">\n                <a href="')
            __M_writer(unicode(_pre))
            __M_writer(u'">&larr; \u4e0a\u4e00\u9875 </a>\n            </li>\n')
        __M_writer(u'    </ul>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 4, "63": 57, "57": 28, "15": 0, "48": 16, "49": 18, "50": 19, "51": 20, "20": 1, "21": 30, "54": 24, "55": 25, "56": 25, "52": 20, "27": 2, "53": 23}, "uri": "/_pager.html", "filename": "/web/kzing.net/hiblog/html/templates/_pager.html"}
__M_END_METADATA
"""
