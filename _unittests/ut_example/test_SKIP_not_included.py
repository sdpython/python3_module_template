"""
@brief      test log(time=100s)

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


class TestSKIPExample(ExtTestCase):
    """Test in SKIP series, skipped by default."""

    def test_src(self):
        self.assertFalse(src is None)

    def test_skip_void(self):
        self.assertTrue(src is not None)


if __name__ == "__main__":
    unittest.main()
