import sys
import os
import datetime
import re
import wild_sphinx_theme

from pyquickhelper.helpgen.default_conf import set_sphinx_variables
set_sphinx_variables(__file__, "project_name", "author(s)", 2016,
                     "wild", wild_sphinx_theme.get_theme_dir(), locals(),
                     extlinks=dict(issue=('https://github.com/sdpython/python3_module_template/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"
