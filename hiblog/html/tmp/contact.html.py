# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414308581.358557
_enable_loop = True
_template_filename = '/web/kzing.net/hiblog/html/templates/contact.html'
_template_uri = '/contact.html'
_source_encoding = 'utf-8'
_exports = []



from _base.setting import CONTACT_TITLE, CONTACT_DESC, CONTACT_CONTENT


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
        __M_writer(u'\r\n\r\n\r\n')
        __M_writer(unicode(base.head()))
        __M_writer(u'\r\n\r\n\r\n<body>\r\n\r\n    ')
        __M_writer(unicode(base.nav()))
        __M_writer(u'\r\n\r\n    <!-- Page Header -->\r\n    <!-- Set your background image for this header on the line below. -->\r\n    <header class="intro-header" style="background-image: url(\'../static/img/contact-bg.jpg\')">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                    <div class="page-heading">\r\n                        <h1>')
        __M_writer(unicode(CONTACT_TITLE))
        __M_writer(u'</h1>\r\n                        <hr class="small">\r\n                        <span class="subheading">')
        __M_writer(unicode(CONTACT_DESC))
        __M_writer(u'</span>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </header>\r\n\r\n    <!-- Main Content -->\r\n    <div class="container">\r\n        <div class="row">\r\n            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\r\n                <p>')
        __M_writer(unicode(CONTACT_CONTENT))
        __M_writer(u'</p>\r\n                <form name="sentMessage" id="contactForm" novalidate>\r\n                    <div class="row control-group">\r\n                        <div class="form-group col-xs-12 floating-label-form-group controls">\r\n                            <label>Name</label>\r\n                            <input type="text" class="form-control" placeholder="Name" id="name" required data-validation-required-message="Please enter your name.">\r\n                            <p class="help-block text-danger"></p>\r\n                        </div>\r\n                    </div>\r\n                    <div class="row control-group">\r\n                        <div class="form-group col-xs-12 floating-label-form-group controls">\r\n                            <label>Email Address</label>\r\n                            <input type="email" class="form-control" placeholder="Email Address" id="email" required data-validation-required-message="Please enter your email address.">\r\n                            <p class="help-block text-danger"></p>\r\n                        </div>\r\n                    </div>\r\n                    <div class="row control-group">\r\n                        <div class="form-group col-xs-12 floating-label-form-group controls">\r\n                            <label>Message</label>\r\n                            <textarea rows="5" class="form-control" placeholder="Message (Support Markdown)" id="message" required data-validation-required-message="Please enter a message."></textarea>\r\n                            <p class="help-block text-danger"></p>\r\n                        </div>\r\n                    </div>\r\n                    <br>\r\n                    <div id="success"></div>\r\n                    <div class="row">\r\n                        <div class="form-group col-xs-12">\r\n                            <button type="submit" class="btn btn-default">Send</button>\r\n                        </div>\r\n                    </div>\r\n                </form>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n    <hr>\r\n\r\n    ')
        __M_writer(unicode(base.footer()))
        __M_writer(u'\r\n\r\n</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 3, "36": 5, "37": 8, "38": 8, "39": 13, "40": 13, "41": 22, "42": 22, "43": 24, "44": 24, "45": 35, "46": 35, "15": 1, "48": 72, "54": 48, "26": 5, "47": 72, "29": 0}, "uri": "/contact.html", "filename": "/web/kzing.net/hiblog/html/templates/contact.html"}
__M_END_METADATA
"""
