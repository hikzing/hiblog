#!/usr/bin/env python
# coding:utf-8
from string import ascii_letters


class IntStr:

    """ 用于将数值型转为较短的字符串.

    用于生成更短更省内存的 redis 键
    """

    #: @param alphabet: 默认的字符编码
    def __init__(self, alphabet=ascii_letters):
        self.alphabet = alphabet
        self.alphabet_reverse = {v: i for i, v in enumerate(alphabet)}
        self.base = len(alphabet)

    def encode(self, n):
        def _encode(n):
            while n:
                n, r = divmod(n, self.base)
                yield self.alphabet[r]
        return ''.join(_encode(n))

    def decode(self, s):
        n = 0
        for c in reversed(s):
            n = n * self.base + self.alphabet_reverse[c]
        return n

int_str = IntStr()
if __name__ == '__main__':
    t = IntStr()
    s = t.encode(123456789)
    print(s)
    print(t.decode(s))
