import sys
import os
import alabaster

source_path = os.path.normpath(
    os.path.join(
        os.path.abspath(
            os.path.split(__file__)[0]),
        ".."))

try:
    from conf_base import *
except ImportError:
    sys.path.append(source_path)
    from conf_base import *

html_theme = 'alabaster'
html_theme_path = ["."]
templates_path = [os.path.join(source_path, 'phdoc_templates')]
html_static_path = ["phdoc_static2"]
blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx2/"
