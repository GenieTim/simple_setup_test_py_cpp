# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
import sysconfig
import warnings
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime

try:
    # this fixes an issue where conda env's site-packages are not available to Sphinx
    paths = sysconfig.get_paths()
    pythonV = "python3.9"
    for key in paths:
        path = paths[key]
        dirname = os.path.basename(path)
        if "python" in dirname and "." in dirname:
            pythonV = dirname
            break

    if (os.getenv("CONDA_PREFIX") is not None):
        newPath = os.path.join(os.getenv("CONDA_PREFIX"),
                               "lib", pythonV, "site-packages")
        sys.path.append(newPath)
    # vgl.: sys.path.insert(
    #     0, "/usr/local/anaconda3/envs/autowig/lib/python3.7/site-packages")
    import simple_setup_test_py_cpp
except ImportError:
    warnings.warn("Failed to import simple_setup_test_py_cpp")


# -- Project information -----------------------------------------------------

project = 'SetupTest'
copyright = '2023-' + datetime.now().strftime('%Y') + ', Tim Bernhard'
author = 'Tim Bernhard'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    # "sphinx.ext.jsmath",
    "sphinx.ext.mathjax"
]

autosummary_generate = True
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../docs-template']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = "index"

# Mathjax options
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"
mathjax3_config = {
    "tex": {
        # "inlineMath": [['$', '$'], ['\\(', '\\)']]
    },
    "extensions": ["jsMath2jax.js"],
    "jax": ["input/TeX"]
}
mathjax_options = {
    "async": "async"
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# add custom css files here, absolute URLS or
# relative to the `html_static_path` directory
html_css_files = [
    'css/custom.css',
]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# Output file base name for HTML help builder.
htmlhelp_basename = "python_exampledoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (
#         master_doc,
#         "python_example.tex",
#         "python_example Documentation",
#         "Sylvain Corlay",
#         "manual",
#     ),
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True
