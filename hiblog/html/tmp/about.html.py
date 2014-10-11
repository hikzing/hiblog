# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1411822384.710238
_enable_loop = True
_template_filename = '/web/kzing.net/html/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='_base.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        base = _mako_get_namespace(context, 'base')
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer(str(base.head(title)))
        __M_writer('\r\n\r\n\r\n<body>\r\n\r\n\r\n    ')
        __M_writer(str(base.nav()))
        __M_writer('\r\n\r\n    <!-- Page Header -->\r\n    <!-- Set your background image for this header on the line below. -->\r\n    <header class="intro-header" style="background-image: url(\'../static/img/about-bg.jpg\')">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                    <div class="page-heading">\r\n                        <h1>About Me</h1>\r\n                        <hr class="small">\r\n                        <span class="subheading">This is what I do.</span>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </header>\r\n\r\n    <!-- Main Content -->\r\n    <div class="container">\r\n        <div class="row">\r\n            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio, adipisci quas excepturi maxime quae totam ducimus consectetur?</p>\r\n                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius praesentium recusandae illo eaque architecto error, repellendus iusto reprehenderit, doloribus, minus sunt. Numquam at quae voluptatum in officia voluptas voluptatibus, minus!</p>\r\n                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nostrum molestiae debitis nobis, quod sapiente qui voluptatum, placeat magni repudiandae accusantium fugit quas labore non rerum possimus, corrupti enim modi! Et.</p>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n    <hr>\r\n\r\n    ')
        __M_writer(str(base.footer()))
        __M_writer('\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "33": 3, "34": 3, "35": 9, "36": 9, "37": 40, "38": 40, "44": 38, "22": 1, "25": 0}, "uri": "about.html", "filename": "/web/kzing.net/html/templates/about.html"}
__M_END_METADATA
"""
