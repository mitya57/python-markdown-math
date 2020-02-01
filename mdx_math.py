# -*- coding: utf-8 -*-

'''
Math extension for Python-Markdown
==================================

Adds support for displaying math formulas using
[MathJax](http://www.mathjax.org/).

Author: 2015-2020, Dmitry Shachnev <mitya57@gmail.com>.
'''

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
from markdown.util import AtomicString, etree


def _wrap_node(node, preview_text, wrapper_tag):
    preview = etree.Element('span', {'class': 'MathJax_Preview'})
    preview.text = AtomicString(preview_text)
    wrapper = etree.Element(wrapper_tag)
    wrapper.extend([preview, node])
    return wrapper


class InlineMathPattern(InlineProcessor):
    def handleMatch(self, m, data):
        node = etree.Element('script')
        node.set('type', self._content_type)
        node.text = AtomicString(m.group(2))
        if self._add_preview:
            node = _wrap_node(node, m.group(0), 'span')
        return node, m.start(0), m.end(0)


class DisplayMathPattern(InlineProcessor):
    def handleMatch(self, m, data):
        node = etree.Element('script')
        node.set('type', '%s; mode=display' % self._content_type)
        if '\\begin' in m.group(1):
            node.text = AtomicString(m.group(0))
        else:
            node.text = AtomicString(m.group(2))
        if self._add_preview:
            node = _wrap_node(node, m.group(0), 'div')
        return node, m.start(0), m.end(0)


class MathExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'enable_dollar_delimiter':
                [False, 'Enable single-dollar delimiter'],
            'add_preview': [False, 'Add a preview node before each math node'],
            'use_asciimath':
                [False, 'Use AsciiMath syntax instead of TeX syntax'],
        }
        super(MathExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        inlinemathpatterns = (
            InlineMathPattern(r'(?<!\\|\$)(\$)([^\$]+)(\$)'),    #  $...$
            InlineMathPattern(r'(?<!\\)(\\\()(.+?)(\\\))')       # \(...\)
        )
        mathpatterns = (
            DisplayMathPattern(r'(?<!\\)(\$\$)([^\$]+)(\$\$)'),  # $$...$$
            DisplayMathPattern(r'(?<!\\)(\\\[)(.+?)(\\\])'),     # \[...\]
            DisplayMathPattern(                            # \begin...\end
                r'(?<!\\)(\\begin{([a-z]+?\*?)})(.+?)(\\end{\2})')
        )
        if not self.getConfig('enable_dollar_delimiter'):
            inlinemathpatterns = inlinemathpatterns[1:]
        if self.getConfig('use_asciimath'):
            mathpatterns = mathpatterns[:-1]  # \begin...\end is TeX only

        add_preview = self.getConfig('add_preview')
        use_asciimath = self.getConfig('use_asciimath')
        content_type = 'math/asciimath' if use_asciimath else 'math/tex'
        for i, pattern in enumerate(mathpatterns):
            pattern._add_preview = add_preview
            pattern._content_type = content_type
            # we should have higher priority than 'escape' which has 180
            md.inlinePatterns.register(pattern, 'math-%d' % i, 185)
        for i, pattern in enumerate(inlinemathpatterns):
            pattern._add_preview = add_preview
            pattern._content_type = content_type
            md.inlinePatterns.register(pattern, 'math-inline-%d' % i, 185)
        if self.getConfig('enable_dollar_delimiter'):
            md.ESCAPED_CHARS.append('$')


def makeExtension(*args, **kwargs):
    return MathExtension(*args, **kwargs)
