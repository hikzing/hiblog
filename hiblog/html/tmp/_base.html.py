# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414309740.784525
_enable_loop = True
_template_filename = u'/web/kzing.net/hiblog/html/templates/_base.html'
_template_uri = u'/_base.html'
_source_encoding = 'utf-8'
_exports = ['head', 'disqus', 'nav', 'footer']



from _base.setting import HOME_TITLE, COPYRIGHT
from _base.config import Config


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>')
        __M_writer(unicode(HOME_TITLE))
        __M_writer(u'</title>\n\n    <!-- Bootstrap Core CSS -->\n    <link href="../static/css/bootstrap.min.css" rel="stylesheet">\n\n    <!-- Custom CSS -->\n    <link href="../static/css/clean-blog.css" rel="stylesheet">\n\n    <!-- For highlight code -->\n    <!-- <link rel="stylesheet" href="../static/css/github.css"/> -->\n    <link rel="stylesheet" href="../static/css/tomorrow.css"/>\n\n</head>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_disqus(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <div id="disqus_thread"></div>\n    <script type="text/javascript">\n        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */\n\n        var disqus_shortname = \'kzing\'; // required: replace example with your forum shortname\n\n        /* * * DON\'T EDIT BELOW THIS LINE * * */\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.type = \'text/javascript\'; dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        this = context.get('this', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n    <!-- Navigation -->\n    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">\n        <div class="container-fluid">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header page-scroll">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n')
        if not this.current_user:
            __M_writer(u'                    <a class="navbar-brand" href="/admin">Admin Login</a>\n')
        else:
            __M_writer(u'                    <a class="navbar-brand" href="/admin">')
            __M_writer(unicode(this.current_user.split('@', 1)[0]))
            __M_writer(u'</a>\n')
        __M_writer(u'            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav navbar-right">\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'">Home</a>\n                    </li>\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'/about">About</a>\n                    </li>\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'/contact">Contact</a>\n                    </li>\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'/sample_post">Sample Post</a>\n                    </li>\n                </ul>\n            </div>\n            <!-- /.navbar-collapse -->\n        </div>\n        <!-- /.container -->\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <!-- Footer -->\n    <footer>\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\n                    <ul class="list-inline text-center">\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-github fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                    </ul>\n                    <p class="copyright text-muted">Copyright &copy; ')
        __M_writer(unicode(COPYRIGHT))
        __M_writer(u' | Powered by <a href="https://github.com/Kzinglzy/hiblog">HiBlog</a></p>\n                </div>\n            </div>\n        </div>\n    </footer>\n\n    <!-- jQuery -->\n    <script src="../static/js/jquery.min.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="../static/js/bootstrap.min.js"></script>\n\n    <!-- Custom Theme JavaScript -->\n    <script src="../static/js/clean-blog.js"></script>\n\n    <!-- Highlight code -->\n    <script src="../static/js/highlight.pack.js"></script>\n    <script >hljs.initHighlightingOnLoad();</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "20": 0, "25": 4, "26": 32, "27": 76, "28": 130, "29": 149, "35": 6, "39": 6, "40": 19, "41": 19, "47": 132, "51": 132, "57": 35, "62": 35, "63": 48, "64": 49, "65": 50, "66": 51, "67": 51, "68": 51, "69": 53, "70": 59, "71": 59, "72": 62, "73": 62, "74": 65, "75": 65, "76": 68, "77": 68, "83": 79, "87": 79, "88": 111, "89": 111, "95": 89}, "uri": "/_base.html", "filename": "/web/kzing.net/hiblog/html/templates/_base.html"}
__M_END_METADATA
"""
