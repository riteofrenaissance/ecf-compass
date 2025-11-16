# docs/conf.py
project = 'ECF Compass'
copyright = '2024, Rite of Renaissance'  # ✅ أضف ' في النهاية
author = 'Samir Baladi'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]

html_theme = 'sphinx_rtd_theme'

# دعم ملفات Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}