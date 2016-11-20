import sys
import os
import datetime
import re


source_path = os.path.normpath(
    os.path.join(
        os.path.abspath(
            os.path.split(__file__)[0])))

try:
    from conf_base import *
except ImportError:
    sys.path.append(source_path)
    from conf_base import *
