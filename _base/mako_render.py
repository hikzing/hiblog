#!/usr/bin/env python
import _env
from os.path import join
from mako.lookup import TemplateLookup


RENDER_PATH = [join(_env.PREFIX, 'html/templates')]

template_lookup = TemplateLookup(
    directories=tuple(RENDER_PATH),
    encoding_errors='ignore',
    input_encoding='utf-8',
    output_encoding='utf-8',
    module_directory=join(_env.PREFIX, 'html/tmp')
)


def mako_render(html, **kwds):

    template = template_lookup.get_template(html)
    return template.render(**kwds)


if __name__ == '__main__':
    print(mako_render('category.html'))
