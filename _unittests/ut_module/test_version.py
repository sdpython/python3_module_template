"""
@brief      test log(time=0s)
"""
import os
import unittest
import re

from python3_module_template import __version__, check


class TestVersion (unittest.TestCase):
    """Test version in *setup.py* is the same in the main *__init__.py*."""

    def test_version(self):
        setup = os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "setup.py")
        with open(setup, "r") as f:
            c = f.read()
        reg = re.compile("sversion *= \\\"(.*)\\\"")

        f = reg.findall(c)
        if len(f) != 1:
            raise Exception("not only one version")
        self.assertEqual(f[0], __version__)

    def test_check(self):
        self.assertTrue(check())


if __name__ == "__main__":
    unittest.main()
