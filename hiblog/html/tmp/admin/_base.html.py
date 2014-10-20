# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413802443.800328
_enable_loop = True
_template_filename = u'/web/kzing.net/hiblog/html/templates/admin/_base.html'
_template_uri = u'admin/_base.html'
_source_encoding = 'utf-8'
_exports = ['head', 'footer', 'nav', 'nav_side']



from _base.config import Config
from model.msg import msg_unread_list


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Welcome, Admin</title>\n\n    <!-- Bootstrap Core CSS -->\n    <link href="../../static/css/bootstrap.min.css" rel="stylesheet">\n\n    <!-- MetisMenu CSS -->\n    <link href="../../static/css/admin/plugins/metisMenu/metisMenu.min.css" rel="stylesheet">\n\n    <!-- Timeline CSS -->\n    <link href="../../static/css/admin/plugins/timeline.css" rel="stylesheet">\n\n    <!-- Custom CSS -->\n    <link href="../../static/css/admin/sb-admin-2.css" rel="stylesheet">\n\n    <!-- Morris Charts CSS -->\n    <link href="../../static/css/admin/plugins/morris.css" rel="stylesheet">\n\n    <!-- Custom Fonts -->\n    <link href="../../static/font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\n\n</head>\n\n')
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


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n        <!-- Navigation -->\n        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'">Back To Home</a>\n            </div>\n            <!-- /.navbar-header -->\n\n            <ul class="nav navbar-top-links navbar-right">\n                <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                        <i class="fa fa-envelope fa-fw"></i>  <i class="fa fa-caret-down"></i>\n                    </a>\n                    <ul class="dropdown-menu dropdown-messages">\n                        ')

        msgs = msg_unread_list()
                                
        
        __M_writer(u'\n')
        if msgs:
            for o in msgs:
                __M_writer(u'                                <li>\n                                    <a href="#">\n                                        <div>\n                                            <strong>')
                __M_writer(unicode(o.user_name))
                __M_writer(u'</strong>\n                                            <span class="pull-right text-muted">\n                                                <em>')
                __M_writer(unicode(o.post_time))
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


def render_nav_side(context,cur_path=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="navbar-default sidebar" role="navigation">\n        <div class="sidebar-nav navbar-collapse">\n            <ul class="nav" id="side-menu">\n                ')

        timeline_active = new_active = msg_active = setting_active = ""
        if cur_path is None:
            timeline_active = "active"
        elif cur_path == "blog_new":
            new_active = "active"
        elif cur_path == "msg":
            msg_active = "active"
        elif cur_path == "setting":
            setting_active = "active"
                        
        
        __M_writer(u'\n                <li>\n                    <a class="')
        __M_writer(unicode(timeline_active))
        __M_writer(u'" href="/admin"><i class="fa fa-dashboard fa-fw"></i>Timeline</a>\n                </li>\n                <li>\n                    <a class = "')
        __M_writer(unicode(new_active))
        __M_writer(u'" href="/admin/blog/edit?new=True"><i class="fa fa-edit fa-fw"></i>New</a>\n                </li>\n                <li>\n                    <a class = "')
        __M_writer(unicode(msg_active))
        __M_writer(u'" href="/admin/msg"><i class="fa  fa-table fa-fw"></i> Message</a>\n                </li>\n                 <li>\n                    <a class = "')
        __M_writer(unicode(setting_active))
        __M_writer(u'" href="/admin/setting"><i class="fa fa-facebook fa-fw"></i> Setting</a>\n                </li>\n            </ul>\n        </div>\n        <!-- /.sidebar-collapse -->\n    </div>\n    <!-- /.navbar-static-side -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "20": 0, "25": 4, "26": 40, "27": 117, "28": 151, "29": 171, "35": 5, "39": 5, "45": 154, "49": 154, "55": 43, "59": 43, "60": 53, "61": 53, "62": 63, "66": 65, "67": 66, "68": 67, "69": 68, "70": 71, "71": 71, "72": 73, "73": 73, "74": 76, "75": 76, "76": 80, "77": 89, "78": 90, "79": 94, "85": 119, "89": 119, "90": 123, "102": 133, "103": 135, "104": 135, "105": 138, "106": 138, "107": 141, "108": 141, "109": 144, "110": 144, "116": 110}, "uri": "admin/_base.html", "filename": "/web/kzing.net/hiblog/html/templates/admin/_base.html"}
__M_END_METADATA
"""
