#!/usr/bin/env python
# coding:utf-8


class Star:

    """使得子类能被double star(**)解包.

    如:
        >>> class Tests(Star):
                a = 1
                b = 2
        >>> test = Test()
        >>> dict(**test)
            {a:1, b:2}
    """

    def keys(self):
        return [attr for attr in self.__class__.__dict__
                if not attr.startswith('__')]

    def __getitem__(self, key):
        return self.__class__.__dict__[key]


if __name__ == '__main__':
    class Test(Star):
        a = 1
        b = 2
    test = Test()
    print(dict(**test))
