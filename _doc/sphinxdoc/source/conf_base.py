# -*- coding: utf-8 -*-
import sys
import os
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
import python3_module_template

source_path = os.path.normpath(os.path.join(
    os.path.abspath(os.path.split(__file__)[0])))

try:
    from conf_base import *
except ImportError:
    sys.path.append(source_path)
    from conf_base import *


set_sphinx_variables(__file__, "python3_module_template", "sdpython", 2019,
                     "sphinx_rtd_theme", None,
                     locals(), book=True,
                     github_repo="https://github.com/sdpython/python3_module_template.git",
                     extlinks=dict(issue=('https://github.com/sdpython/python3_module_template/issues/%s', 'issue')),
                     doc_version=python3_module_template.__version__)

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet(),
}

nblinks = {'slideshowrst': 'http://www.xavierdupre.fr/'}


def custom_latex_processing(latex):
    """
    process a latex file and returned the modified version

    @param      latex       string
    @return                 string
    """
    if latex is None:
        raise ValueError("Latex is null")
    # this weird modification is only needed when jenkins run a unit test in
    # pyquickhelper (pycode)
    return latex
