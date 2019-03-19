"""
@brief      test tree node (time=25s)
"""

import os
import unittest
from pyquickhelper.pycode import coverage_combine, get_temp_folder, ExtTestCase


class TestCoverageCombine(ExtTestCase):

    def test_coverage_combine(self):

        temp = get_temp_folder(__file__, "temp_coverage_combine")
        source = os.path.normpath(os.path.abspath(
            os.path.join(temp, "..", "..", "..", "src")))
        covs = [os.path.join(temp, "..", "data", "cov%d.txt" % i)
                for i in range(1, 3)]
        coverage_combine(covs, temp, source=source)
        index = os.path.join(temp, "index.html")
        self.assertExists(index)


if __name__ == "__main__":
    unittest.main()
