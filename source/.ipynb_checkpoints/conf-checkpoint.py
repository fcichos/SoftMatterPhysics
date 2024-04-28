# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Soft Matter Lecture'
copyright = '2023, Frank Cichos, Ralf Seidel'
author = 'Frank Cichos, Ralf Seidel'
master_doc = 'index'

# The full version, including alpha/beta/rc tags
release = '23'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
]

# Add any paths that contain templates here, relative to this directory.
exclude_patterns = ['_build', '**.ipynb_checkpoints']
templates_path = ['_templates']

mathjax3_config = {
'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_rtd_theme

html_theme = 'furo'
# html_theme_path = [furo.get_html_theme_path()]

#def setup(app):
#    app.add_stylesheet('theme_overrides.css')

# html_logo = 'img/HY-logo-2017.png'

# Add last modified to all pages
html_last_updated_fmt = ""

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme_options = {
#    "collapse_navigation" : True
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'fcichos',
    'github_repo': 'SoftMatterPhysics',
    'github_version': 'main/',
    'conf_py_path': '/source/'
}

html_logo = 'img/mona_logo.png'

# -- Extension configuration -------------------------------------------------
# This is processed by Jinja2 and inserted before each notebook

nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=False) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::
        This page was generated from `{{ docname }}`.
        :raw-html:`<br/><a href="https://mybinder.org/v2/gh/fcichos/SoftMatterPhysics/main?urlpath=tree/source/{{ docname }}"><img alt="Binder badge" src="https://img.shields.io/badge/launch-full%20binder-red.svg" style="vertical-align:text-bottom"></a>`
        :raw-html:`<br/><a href="https://colab.research.google.com/github/fcichos/SoftMatterPhysics/blob/main/build/html/{{ docname }}"><img alt="Colab badge" src="https://colab.research.google.com/assets/colab-badge.svg" style="vertical-align:text-bottom"></a>`
        You can download the PDF-Version of this page using the link below.
        :raw-html:`<br/><a href="https://raw.githubusercontent.com/fcichos/SoftMatterPhysics/main/source/{{ docname }}"</a>`

.. only:: latex

    The following section was created from :file:`{{ docname }}`.
"""

nbsphinx_allow_errors = True

# Sphinx versioning settings
scv_show_banner = True
scv_whitelist_branches = ('main', 'develop')
