#!/usr/bin/env python3

from markdown import Markdown
import unittest

class MathTestCase(unittest.TestCase):
    def verify(self, mkd_name, html_name, config=None):
        config = config or dict()
        md = Markdown(extensions=['mdx_math'], extension_configs={'mdx_math': config})
        with open('test_data/%s.mkd' % mkd_name) as mkd_file:
            mkd = mkd_file.read()
        with open('test_data/%s.html' % html_name) as html_file:
            html = html_file.read()
        self.assertEqual(html, md.convert(mkd) + '\n')

    def r(mkd_name, html_name, **config):
        return lambda self: self.verify(mkd_name, html_name, config=config)

    test_inline_latex = r('inline_latex', 'inline')
    test_inline_latex_escaped = r('inline_latex_escaped', 'inline_latex_escaped')
    test_inline_latex_preview = r('inline_latex', 'inline_preview', add_preview=True)
    test_inline_tex = r('inline_tex', 'inline', enable_dollar_delimiter=True)
    test_inline_tex_disabled = r('inline_tex', 'inline_tex_disabled')
    test_inline_tex_escaped = r('inline_tex_escaped', 'inline_tex_escaped', enable_dollar_delimiter=True)
    test_inline_inside_code = r('inline_latex_inside_code', 'inline_latex_inside_code')
    test_inline_inside_standalone = r('inline_inside_standalone', 'inline_inside_standalone')
    test_inline_gitlab = r('inline_gitlab', 'inline', use_gitlab_delimiters=True)
    test_standalone_latex = r('standalone_latex', 'standalone')
    test_standalone_latex_escaped = r('standalone_latex_escaped', 'standalone_latex_escaped')
    test_standalone_latex_preview = r('standalone_latex', 'standalone_preview', add_preview=True)
    test_standalone_tex = r('standalone_tex', 'standalone')
    test_standalone_gitlab = r('standalone_gitlab', 'standalone_gitlab', use_gitlab_delimiters=True)
    test_standalone_gitlab_nested = r('standalone_gitlab_nested', 'standalone_gitlab_nested', use_gitlab_delimiters=True)
    test_begin_end = r('beginend', 'beginend')
    test_begin_end_preview = r('beginend', 'beginend_preview', add_preview=True)
    test_begin_end_inside_inline = r('beginend_inside_inline', 'beginend_inside_inline')
    test_begin_end_inside_standalone = r('beginend_inside_standalone', 'beginend_inside_standalone')
    test_inline_asciimath = r('inline_asciimath', 'inline_asciimath', use_asciimath=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
