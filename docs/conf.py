"""
Configuration de la documentation Sphinx pour py_stats_toolkit.
"""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Informations du projet -------------------------------------------------

project = 'Py Stats Toolkit'
copyright = '2024, PhoenixProject'
author = 'PhoenixProject'

# La version complète, incluant alpha/beta/rc tags
release = '1.0.0'

# -- Configuration générale -------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options pour la sortie HTML -------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# -- Options pour l'extension autodoc --------------------------------------

autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'

# -- Options pour l'extension napoleon ------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# -- Options pour l'extension intersphinx ---------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'seaborn': ('https://seaborn.pydata.org/', None),
}

# -- Options pour la sortie LaTeX -----------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',
}

# -- Options pour la sortie man -------------------------------------------

man_pages = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     [author], 1)
]

# -- Options pour la sortie texinfo ---------------------------------------

texinfo_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie epub ------------------------------------------

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']

# -- Options pour la sortie PDF -------------------------------------------

pdf_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation', author)
]

# -- Options pour la sortie HTMLHelp --------------------------------------

htmlhelp_basename = 'py_stats_toolkitdoc'

# -- Options pour la sortie qthelp ----------------------------------------

qthelp_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit'),
]

# -- Options pour la sortie devhelp ---------------------------------------

devhelp_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie applehelp -------------------------------------

applehelp_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie json ------------------------------------------

json_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie xml -------------------------------------------

xml_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie yaml ------------------------------------------

yaml_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie pickle ----------------------------------------

pickle_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie dirhtml ---------------------------------------

dirhtml_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie singlehtml ------------------------------------

singlehtml_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie changes ---------------------------------------

changes_documents = [
    ('index', 'py_stats_toolkit', 'Py Stats Toolkit Documentation',
     author, 'py_stats_toolkit', 'Une bibliothèque Python pour l\'analyse statistique',
     'Miscellaneous'),
]

# -- Options pour la sortie linkcheck -------------------------------------

linkcheck_ignore = [
    r'http://localhost:\d+/',
    r'http://127.0.0.1:\d+/',
]

# -- Options pour la sortie doctest ---------------------------------------

doctest_global_setup = '''
import numpy as np
import pandas as pd
from py_stats_toolkit import *
'''

# -- Options pour la sortie coverage --------------------------------------

coverage_ignore_modules = [
    'py_stats_toolkit.tests',
]

# -- Options pour la sortie viewcode --------------------------------------

viewcode_import = True

# -- Options pour la sortie todo ------------------------------------------

todo_include_todos = True

# -- Options pour la sortie autosummary -----------------------------------

autosummary_generate = True

# -- Options pour la sortie graphviz --------------------------------------

graphviz_output_format = 'png'

# -- Options pour la sortie inheritance_graph -----------------------------

inheritance_graph_attrs = dict(rankdir="TB", size='"6.0, 4.0"',
                              fontsize=14, ratio='compress')

# -- Options pour la sortie inheritance_diagram ---------------------------

inheritance_diagram_attrs = dict(rankdir="TB", size='"6.0, 4.0"',
                                fontsize=14, ratio='compress')

# -- Options pour la sortie numpydoc -------------------------------------

numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = True
numpydoc_class_members_toctree = True
numpydoc_use_plots = True

# -- Options pour la sortie sphinx_autodoc_typehints ---------------------

typehints_fully_qualified = False
typehints_document_rtype = True

# -- Options pour la sortie sphinx_autodoc_typehints ---------------------

typehints_fully_qualified = False
typehints_document_rtype = True

# -- Options pour la sortie sphinx_autodoc_typehints ---------------------

typehints_fully_qualified = False
typehints_document_rtype = True 