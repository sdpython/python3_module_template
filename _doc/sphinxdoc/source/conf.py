#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  documentation build configuration file, created by
# sphinx-quickstart on Fri May 10 18:35:14 2013.
#

import sys, os, datetime, re
import wild_sphinx_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0], "project_name")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0], "..", "..", "..", "..", "pyquickhelper", "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables
set_sphinx_variables(   __file__,
                        "project_name",
                        "author(s)",
                        2014,
                        "wild",
                        wild_sphinx_theme.get_theme_dir(),
                        locals())