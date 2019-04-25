"""
@brief      test tree node (time=50s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from python3_module_template import check, _setup_hook


class TestSetup(ExtTestCase):

    def test_check(self):
        self.assertTrue(check())

    def test_setup_hook(self):
        _setup_hook()


if __name__ == "__main__":
    unittest.main()
