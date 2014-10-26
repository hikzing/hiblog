#!/usr/bin/env python
# coding:utf-8
from markdown import markdown


def turn_to_markdown(content):
    return markdown(content)  # TODO


if __name__ == '__main__':
    content = '#title\n**strong**\n'
    print(turn_to_markdown(content))
