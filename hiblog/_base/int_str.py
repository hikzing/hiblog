#!/usr/bin/env python
# coding:utf-8

#
# Thanks much to my tutor zsp : )
#

from string import ascii_uppercase


class IntStr:

    def __init__(self, alphabet=ascii_uppercase, sign_character=None):
        """ 将数字转为更短的字符. 可用于生成更短的redis key以减少内存占用或短 url

        @param: alphabet 预定义的短字符集合
        """
        self.alphabet = alphabet
        self.sign_character = sign_character
        self._base = len(alphabet)

        # 键和键对应的索引的字典
        self._alphabet_index = {value: index for index, value in enumerate(alphabet)}

    def encode(self, num):
        """ 将数值转为短字符串
        """
        sign = self.sign_character
        if num < 0:
            if sign:
                return sign + self.encode(-num)
            else:
                raise Exception('should give a sign character when num is below zero')

        result = []
        while num:
            num, r = divmod(num, self._base)
            result.append(self.alphabet[r])

        return ''.join(reversed(result))

    def decode(self, s):
        """ 将短字符串还原为原始数值
        """
        sign = self.sign_character
        if sign and s.startswith(sign):
            return -self.decode(s[len(sign):])
        n = 0
        for c in s:
            n = n * self._base + self._alphabet_index[c]

        return n

int_str = IntStr()
