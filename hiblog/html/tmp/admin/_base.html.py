# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413456329.39943
_enable_loop = True
_template_filename = u'/web/kzing.net/hiblog/html/templates/admin/_base.html'
_template_uri = u'admin/_base.html'
_source_encoding = 'utf-8'
_exports = ['head', 'nav', 'footer']



# from model.msg import msg_unread_list
from model.msg import msg_unread_list


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
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
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Admin</title>\n\n    <!-- Bootstrap Core CSS -->\n    <link href="../../static/css/bootstrap.min.css" rel="stylesheet">\n\n    <!-- MetisMenu CSS -->\n    <link href="../../static/css/admin/plugins/metisMenu/metisMenu.min.css" rel="stylesheet">\n\n    <!-- Timeline CSS -->\n    <link href="../../static/css/admin/plugins/timeline.css" rel="stylesheet">\n\n    <!-- Custom CSS -->\n    <link href="../../static/css/admin/sb-admin-2.css" rel="stylesheet">\n\n    <!-- Morris Charts CSS -->\n    <link href="../../static/css/admin/plugins/morris.css" rel="stylesheet">\n\n    <!-- Custom Fonts -->\n    <link href="../../static/font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\n\n</head>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n        <!-- Navigation -->\n        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.html">Admin</a>\n            </div>\n            <!-- /.navbar-header -->\n\n            <ul class="nav navbar-top-links navbar-right">\n                <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                        <i class="fa fa-envelope fa-fw"></i>  <i class="fa fa-caret-down"></i>\n                    </a>\n                    <ul class="dropdown-menu dropdown-messages">\n                        ')

        msgs = msg_unread_list()
                                
        
        __M_writer(u'\n')
        if msgs:
            for o in msgs:
                __M_writer(u'                                <li>\n                                    <a href="#">\n                                        <div>\n                                            <strong>')
                __M_writer(unicode(o.user_name))
                __M_writer(u'</strong>\n                                            <span class="pull-right text-muted">\n                                                <em>')
                __M_writer(unicode(o.format_time))
                __M_writer(u'</em>\n                                            </span>\n                                        </div>\n                                        <div>')
                __M_writer(unicode(o.msg_summarize))
                __M_writer(u'</div>\n                                    </a>\n                                </li>\n')
            __M_writer(u'\n                            <li class="divider"></li>\n                            <li>\n                                <a class="text-center" href="#">\n                                    <strong>Read All Messages</strong>\n                                    <i class="fa fa-angle-right"></i>\n                                </a>\n                            </li>\n\n')
        else:
            __M_writer(u'                            <li>\n                                <strong class="text-center"> No Messages Receive</strong>\n                            </li>\n')
        __M_writer(u'                    </ul>\n                    <!-- /.dropdown-messages -->\n                </li>\n                <!-- /.dropdown -->\n                <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                        <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n                    </a>\n                    <ul class="dropdown-menu dropdown-user">\n                        <li><a href="#"><i class="fa fa-user fa-fw"></i> User Profile</a>\n                        </li>\n                        <li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n                        </li>\n                        <li class="divider"></li>\n                        <li><a href="login.html"><i class="fa fa-sign-out fa-fw"></i> Logout</a>\n                        </li>\n                    </ul>\n                    <!-- /.dropdown-user -->\n                </li>\n                <!-- /.dropdown -->\n            </ul>\n            <!-- /.navbar-top-links -->\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <!-- jQuery Version 1.11.0 -->\n    <script src="../../static/js/jquery.min.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="../../static/js/bootstrap.min.js"></script>\n\n    <!-- Metis Menu Plugin JavaScript -->\n    <script src="../../static/js/admin/plugins/metisMenu/metisMenu.min.js"></script>\n\n    <!-- Morris Charts JavaScript -->\n    <script src="../../static/js/admin/plugins/morris/raphael.min.js"></script>\n    <script src="../../static/js/admin/plugins/morris/morris.min.js"></script>\n    <script src="../../static/js/admin/plugins/morris/morris-data.js"></script>\n\n    <!-- Custom Theme JavaScript -->\n    <script src="../../static/js/admin/sb-admin-2.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "20": 0, "25": 4, "26": 40, "27": 117, "28": 136, "34": 5, "38": 5, "44": 43, "48": 43, "49": 63, "53": 65, "54": 66, "55": 67, "56": 68, "57": 71, "58": 71, "59": 73, "60": 73, "61": 76, "62": 76, "63": 80, "64": 89, "65": 90, "66": 94, "72": 119, "76": 119, "82": 76}, "uri": "admin/_base.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/_base.html"}
__M_END_METADATA
"""
