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

from src.python3_module_template.subproject.myexampleb import onefunction


class TestExample(ExtTestCase):
    """Third  example of a test."""

    def test_src(self):
        "skip pylint"
        self.assertFalse(src is None)

    def test_onefunction(self):
        self.assertTrue(onefunction(3, 4), 7)
        with self.assertRaises(TypeError):
            onefunction(3.3, 4)


if __name__ == "__main__":
    unittest.main()
