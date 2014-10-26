#!/usr/bin/env python
#coding:utf-8
import _env
from hiblog.model.password import Password
from hiblog.model.re_mail import RE_MAIL
from hiblog.model.admin import is_admin, admin_new


def admin_guide():

    def _mail_verify(mail):

        if not RE_MAIL.match(mail):
            print("请输入正确的邮箱")
        elif is_admin(mail):
            print("用户已存在")
        else:
            return True
        return False

    def _password_verify(password):
        if len(password) < 6:
            print("密码至少为6位")
            return False
        return True

    def _raw_input(desc, quit={'quit', 'q'}):
        """ 给原始的raw_input 函数加上退出功能
        """
        data = raw_input(desc)
        if data in quit:
            exit()  # 结束整个程序
        return data

    print("######## 创建新用户, 输入 quit 或者 q 退出 #######\n")

    mail_ok = password_ok = False
    while True:
        if not mail_ok:
            mail = _raw_input("$请输入邮箱: ")
            mail_ok = _mail_verify(mail)

        elif mail_ok and not password_ok:
            password = _raw_input("$请输入密码: ")
            password_ok = _password_verify(password)

        elif mail_ok and password_ok:
            assert mail and password
            Password.new(mail, password)
            admin_new(mail)
            break

    print("##### 账户创建成功 #####")


if __name__ == '__main__':
    admin_guide()
