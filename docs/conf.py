# docs/conf.py
project = 'ECF Compass'
copyright = '2024, Rite of Renaissance'
author = 'Samir Baladi'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# دعم ملفات Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}