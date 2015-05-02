Math extension for Python-Markdown
==================================

This extension adds math formulas support to [Python-Markdown]
(works with version 2.6 or newer).

[Python-Markdown]: https://github.com/waylan/Python-Markdown

Installation
------------

Use `setup.py build` and `setup.py install` to build and install this
extension, respectively.

The extension name is `mdx_math`, so you need to add that name to your
list of Python-Markdown extensions.
Check [Python-Markdown documentation] for details on how to load
extensions.

[Python-Markdown documentation]: http://pythonhosted.org/Markdown/extensions/

Usage
-----

To use this extension, you need to include [MathJax] library in HTML files, like:

    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js"></script>

[MathJax]: http://www.mathjax.org/

Also, you need to specify a configuration for MathJax. Please note that
most of standard configuratons include `tex2jax` extension, which is not needed
with this code.

Example of MathJax configuration:

    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      config: ["MMLorHTML.js"],
      jax: ["input/TeX", "output/HTML-CSS", "output/NativeMML"],
      extensions: ["MathMenu.js", "MathZoom.js"]
    });
    </script>

Math Delimiters
---------------

For inline math, use `\(...\)`.

For standalone math, use `$$...$$`, `\[...\]` or `\begin...\end`.

The single-dollar delimiter (`$...$`) for inline math is disabled by
default, but can be enabled by passing `enable_dollar_delimiter=True`
in the extension configuration.

Notes
-----

If you use [ReText](http://retext.sourceforge.net/), this extension is not needed as it is
included by default.
