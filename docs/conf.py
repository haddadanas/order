# coding: utf-8

import sys
import os


thisdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(thisdir, "_extensions"))
sys.path.insert(0, os.path.dirname(thisdir))

import order as od


project = od.__name__
author = od.__author__
copyright = od.__copyright__
copyright = copyright[10:] if copyright.startswith("Copyright ") else copyright
version = od.__version__[:od.__version__.index(".", 2)]
release = od.__version__
language = "en"

templates_path = ["_templates"]
html_static_path = ["_static"]
master_doc = "index"
source_suffix = ".rst"
exclude_patterns = []
pygments_style = "sphinx"
add_module_names = False

html_title = "{} v{}".format(project, version)
html_logo = "../logo240.png"
html_sidebars = {"**": [
    "about.html",
    "localtoc.html",
    "searchbox.html",
]}
html_theme = "sphinx_rtd_theme"
html_theme_options = {}
if html_theme == "sphinx_rtd_theme":
    html_theme_options.update({
        "logo_only": True,
        "prev_next_buttons_location": None,
        "collapse_navigation": False,
    })
elif html_theme == "alabaster":
    html_theme_options.update({
        "github_user": "riga",
        "github_repo": "order",
        "travis_button": True,
    })

extensions = ["sphinx.ext.autodoc", "pydomain_patch"]

autodoc_member_order = "bysource"


def setup(app):
    app.app.add_css_file("styles_common.css")
    if html_theme in ("sphinx_rtd_theme", "alabaster"):
        app.app.add_css_file("styles_{}.css".format(html_theme))
