#!/usr/bin/env python
# coding:utf-8
import re

RE_MAIL = re.compile(r'^\w+[-+.\w]*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')

if __name__ == '__main__':
    mail = 'kzing@gmail.com'
    print(RE_MAIL.match(mail))
