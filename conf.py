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
import sphinx_rtd_theme
import recommonmark

# -- Project information -----------------------------------------------------

project = 'vfxim-docs'
copyright = '2020, Netherlands Film Academy'
author = 'Bo Kamphues'

# The full version, including alpha/beta/rc tags
release = '0.2.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    'recommonmark'
]

# The master toctree document.
master_doc = 'index'

show_authors = True

# Translate options
gettext_uuid = True
gettext_compact = False
locale_dirs = ['locales']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

locale_dirs = ['locale/']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['README.md', 'template.rst']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_logo = "logo.svg"

# RTD Theme options:
html_theme_options = {
    'titles_only': False,
    'logo_only': True
}

html_last_updated_fmt = ''