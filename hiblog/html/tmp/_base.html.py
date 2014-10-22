# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413969408.984805
_enable_loop = True
_template_filename = u'/web/kzing.net/hiblog/html/templates/_base.html'
_template_uri = u'/_base.html'
_source_encoding = 'utf-8'
_exports = ['head', 'disqus', 'nav', 'footer']



from _base.config import Config, Prepare


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


def render_head(context,title):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>')
        __M_writer(unicode(title))
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
        __M_writer(unicode(Prepare.name))
        __M_writer(u' Powered by <a href="https://github.com/Kzinglzy/hiblog">HiBlog</a></p>\n                </div>\n            </div>\n        </div>\n    </footer>\n\n    <!-- jQuery -->\n    <script src="../static/js/jquery.min.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="../static/js/bootstrap.min.js"></script>\n\n    <!-- Custom Theme JavaScript -->\n    <script src="../static/js/clean-blog.js"></script>\n\n    <!-- Highlight code -->\n    <script src="../static/js/highlight.pack.js"></script>\n    <script >hljs.initHighlightingOnLoad();</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "19": 0, "24": 3, "25": 31, "26": 75, "27": 129, "28": 148, "34": 5, "38": 5, "39": 18, "40": 18, "46": 131, "50": 131, "56": 34, "61": 34, "62": 47, "63": 48, "64": 49, "65": 50, "66": 50, "67": 50, "68": 52, "69": 58, "70": 58, "71": 61, "72": 61, "73": 64, "74": 64, "75": 67, "76": 67, "82": 78, "86": 78, "87": 110, "88": 110, "94": 88}, "uri": "/_base.html", "filename": "/web/kzing.net/hiblog/html/templates/_base.html"}
__M_END_METADATA
"""
