[![Build Status](https://github.com/mitya57/python-markdown-math/actions/workflows/main.yml/badge.svg)][Actions]

[Actions]: https://github.com/mitya57/python-markdown-math/actions

Math extension for Python-Markdown
==================================

This extension adds math formulas support to [Python-Markdown].

[Python-Markdown]: https://github.com/Python-Markdown/markdown

Installation
------------

### Install from PyPI

```
$ pip install python-markdown-math
```

### Install locally

Use `pip install .` to install this extension from a local Git checkout.

The extension name is `mdx_math`, so you need to add that name to your
list of Python-Markdown extensions.
Check [Python-Markdown documentation] for details on how to load
extensions.

[Python-Markdown documentation]: https://python-markdown.github.io/reference/#extensions

Usage
-----

To use this extension, you need to include [MathJax] library in HTML files, like:

```html
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js">
</script>
```

[MathJax]: https://www.mathjax.org/

Also, you need to specify a configuration for MathJax. Please note that
most of standard configurations include `tex2jax` extension, which is not needed
with this code.

Example of configuration for MathJax 2.x:

```html
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  config: ["MMLorHTML.js"],
  jax: ["input/TeX", "output/HTML-CSS", "output/NativeMML"],
  extensions: ["MathMenu.js", "MathZoom.js"]
});
</script>
```

If you want to use MathJax 3.x, you need to teach it to understand 2.x-style
`<script>` tags. See the [upgrading documentation] on how to do it.
Alternatively, you may use the [Arithmatex] extension which has a generic
output mode, that does not require such special configuration.

To pass the extension to Python-Markdown, use `mdx_math` as extension name.
For example:

```python
>>> md = markdown.Markdown(extensions=['mdx_math'])
>>> md.convert('$$e^x$$')
'<p>\n<script type="math/tex; mode=display">e^x</script>\n</p>'
```

Usage from the command line:

```
$ echo "\(e^x\)" | python3 -m markdown -x mdx_math
<p>
<script type="math/tex">e^x</script>
</p>
```

[upgrading documentation]: https://docs.mathjax.org/en/latest/upgrading/v2.html#math-script-example
[Arithmatex]: https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/

Math Delimiters
---------------

For inline math, use `\(...\)`.

For standalone math, use `$$...$$`, `\[...\]` or `\begin...\end`.

The single-dollar delimiter (`$...$`) for inline math is disabled by
default, but can be enabled by passing `enable_dollar_delimiter=True`
in the extension configuration.

If you want to use [GitLab-style delimiters] (``$`...`$`` for inline math,
and a code block-like `` ```math...``` `` syntax for standalone), use
`use_gitlab_delimiters=True` configuration option.

If you want to this extension to generate a preview node (which will be shown
when MathJax has not yet processed the node, or when JavaScript is unavailable),
use `add_preview=True` configuration option.

[GitLab-style delimiters]: https://docs.gitlab.com/user/markdown/#math-equations

Notes
-----

If you use [ReText](https://github.com/retext-project/retext), this extension
is not needed as it is included by default.

This extension also works with Katex.  Use the following in your page `<head>`:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>
```
