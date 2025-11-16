# docs/conf.py
project = 'ECF Compass'
copyright = '2024, Rite of Renaissance'
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

# تحديد الملف الرئيسي (إذا كان index.md)
master_doc = 'index'

# المسارات
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# اللغة
language = 'ar'

# إعدادات إضافية للغة العربية
html_search_language = 'ar'