import sys
import os
import datetime
import re
import wild_sphinx_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables
set_sphinx_variables(__file__,
                     "project_name",
                     "author(s)",
                     2014,
                     "wild",
                     wild_sphinx_theme.get_theme_dir(),
                     locals())

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"