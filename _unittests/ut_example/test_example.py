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

from src.python3_module_template.subproject.myexample import myclass
from src.python3_module_template.subproject.myexampleb import myclassb
from src.python3_module_template.subproject2.myexample2 import myclass2


class TestExample(ExtTestCase):
    """Example of a test."""

    def test_src(self):
        "skip pylint"
        self.assertFalse(src is None)

    def test_split_cmp_command(self):
        my = myclass(4)
        r = my.get_value(5)
        ex = 20
        if r != ex:
            raise Exception("we expect %f, not %f" % (ex, r))
        my2 = myclass2(5)
        my3 = myclassb(4)
        self.assertTrue(my2 is not None)
        self.assertTrue(my3 is not None)
        mul = my2.get_value(3)
        self.assertEqual(mul, 15)


if __name__ == "__main__":
    unittest.main()
