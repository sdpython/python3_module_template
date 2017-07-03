"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest

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

from pyquickhelper.loghelper import fLOG
from src.project_name.subproject.myexampleb import onefunction


class TestExample (unittest.TestCase):

    def test_onefunction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(onefunction(3, 4), 7)
        with self.assertRaises(TypeError):
            onefunction(3.3, 4)


if __name__ == "__main__":
    unittest.main()
