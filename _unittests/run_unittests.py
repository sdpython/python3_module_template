"""
@file
@brief run all unit tests
"""

import unittest
import os
import sys
import io


def main():
    try:
        import pyquickhelper
    except ImportError:
        sys.path.append(
            os.path.normpath(
                os.path.abspath(
                    os.path.join(
                        os.path.split(__file__)[0],
                        "..",
                        "..",
                        "pyquickhelper",
                        "src"))))
        if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
            sys.path.append(os.environ["PYQUICKHELPER"])
        import pyquickhelper

    from pyquickhelper import fLOG, run_cmd, main_wrapper_tests
    fLOG(OutputPrint=True)
    main_wrapper_tests(__file__)

if __name__ == "__main__":
    main()
