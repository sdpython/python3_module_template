"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.pycode import ExtTestCase

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.python3_module_template.subproject.myexampleb import myclassb
from src.python3_module_template.subproject2.myexample2 import myclass2
from src.python3_module_template import _setup_hook


class TestExampleExt(ExtTestCase):
    """Second example of a test."""

    def test_src(self):
        self.assertFalse(src is None)

    def test_static(self):
        self.assertTrue(myclass2.static_example() is not None)
        cl = myclass2(1)
        self.assertTrue(cl.property_example is not None)

    def test_hook(self):
        _setup_hook()

    def test_myclassb(self):
        b = myclassb(1)
        c = b.method_napoleon(1, 2)
        self.assertEqual(c, 3)


if __name__ == "__main__":
    unittest.main()
