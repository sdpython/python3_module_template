"""
@brief      test log(time=0s)
"""

import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import explore_folder_iterfile
from pyquickhelper.ipythonhelper import upgrade_notebook, remove_execution_number


class TestConvertNotebooks(unittest.TestCase):
    """Converts notebooks from v3 to v4. Should not be needed anymore."""

    def test_convert_notebooks(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.dirname(__file__))
        fold2 = os.path.normpath(
            os.path.join(fold, "..", "..", "_doc", "notebooks"))
        for nbf in explore_folder_iterfile(fold2, pattern=".*[.]ipynb"):
            t = upgrade_notebook(nbf)
            if t:
                fLOG("modified", nbf)
            # remove numbers
            remove_execution_number(nbf, nbf)

        fold2 = os.path.normpath(os.path.join(fold, "..", "..", "_unittests"))
        for nbf in explore_folder_iterfile(fold2, pattern=".*[.]ipynb"):
            t = upgrade_notebook(nbf)
            if t:
                fLOG("modified", nbf)


if __name__ == "__main__":
    unittest.main()
