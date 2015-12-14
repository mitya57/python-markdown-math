#!/usr/bin/env python3

from markdown import Markdown
import unittest

class MathTestCase(unittest.TestCase):
    def verify(self, mkd_name, html_name, enable_dollar_delimiter=False):
        config = {'enable_dollar_delimiter': enable_dollar_delimiter}
        md = Markdown(extensions=['mdx_math'], extension_configs={'mdx_math': config})
        with open('test_data/%s.mkd' % mkd_name) as mkd_file:
            mkd = mkd_file.read()
        with open('test_data/%s.html' % html_name) as html_file:
            html = html_file.read()
        self.assertEqual(html, md.convert(mkd) + '\n')

    def r(*args):
        return lambda self: self.verify(*args)

    test_inline_latex = r('inline_latex', 'inline')
    test_inline_latex_escaped = r('inline_latex_escaped', 'inline_latex_escaped')
    test_inline_tex = r('inline_tex', 'inline', True)
    test_inline_tex_disabled = r('inline_tex', 'inline_tex_disabled')
    test_inline_inside_code = r('inline_latex_inside_code', 'inline_latex_inside_code')
    test_standalone_latex = r('standalone_latex', 'standalone')
    test_standalone_latex_escaped = r('standalone_latex_escaped', 'standalone_latex_escaped')
    test_standalone_tex = r('standalone_tex', 'standalone')
    test_begin_end = r('beginend', 'beginend')

if __name__ == '__main__':
    unittest.main(verbosity=2)
