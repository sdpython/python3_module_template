# coding: latin-1
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
from src.project_name.subproject.myexampleb import myclassb
from src.project_name.subproject2.myexample2 import myclass2
from src.project_name import _setup_hook


class TestExampleExt (unittest.TestCase):

    def test_static(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)

        fLOG("comment to test fLOG")
        assert myclass2.static_example()
        cl = myclass2(1)
        assert cl.property_example

    def test_hook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        _setup_hook()

    def test_myclassb(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        b = myclassb(1)
        c = b.method_napoleon(1, 2)
        self.assertEqual(c, 3)


if __name__ == "__main__":
    unittest.main()
