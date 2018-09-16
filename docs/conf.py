# -*- coding: utf-8 -*-

project = 'curandera'
copyright = 'Isabella Muerte'
author = 'Isabella Muerte'
version = '0.1'
release = '0.1'

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
]

source_suffix = '.rst'
master_doc = 'index'

language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

extlinks = {
    'github': ('https://github.com/%s', '')
    'issue': ('https://github.com/slurps-mad-rips/curandera/issues/%s', 'issue ')
}

todo_include_todos = True