#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(name='python-markdown-math',
      description='Math extension for Python-Markdown',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Dmitry Shachnev',
      author_email='mitya57@gmail.com',
      version='0.6',
      url='https://github.com/mitya57/python-markdown-math',
      py_modules=['mdx_math'],
      entry_points={
          'markdown.extensions': [
              'mdx_math = mdx_math:MathExtension',
          ],
      },
      license='BSD')
