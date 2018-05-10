
.. _l-README:

README
======

.. image:: https://travis-ci.org/sdpython/python3_module_template.svg?branch=master
    :target: https://travis-ci.org/sdpython/python3_module_template
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/8yv4brsckay4374a?svg=true
    :target: https://ci.appveyor.com/project/sdpython/python3-module-template
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/python3_module_template/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/python3_module_template/tree/master

.. image:: https://badge.fury.io/py/python3_module_template.svg
    :target: http://badge.fury.io/py/python3_module_template

.. image:: http://img.shields.io/github/issues/sdpython/python3_module_template.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/python3_module_template/issues

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://coveralls.io/repos/sdpython/python3_module_template/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/sdpython/python3_module_template?branch=master

.. image:: https://requires.io/github/sdpython/python3_module_template/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/python3_module_template/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/python3_module_template/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/python3_module_template?branch=master

.. image:: http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

**Links:**

* `GitHub/python3_module_template <https://github.com/sdpython/python3_module_template/>`_
* `documentation <http://www.xavierdupre.fr/app/python3_module_template/helpsphinx2/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/blog/main_0000.html#ap-main-0>`_

Quick start
-----------

* install: ``python setup.py install``
* documentation: ``python setup.py build_sphinx``
* unit tests: ``python setup.py unittests``

Introduction
------------

This project is a skeleton for any new project. It contains:

* a source folder: ``src``
* a unit test folder: ``_unittests``, go to this folder and run ``run_unittests.py``
* a _doc folder: ``_doc``, it will contains the documentation
* a file ``setup.py`` to build and to install the module

All theses steps were only tested on Windows. Suppot for linux will be added later.
To create your own project, you need to rename the folder ``python3_module_template`` in ``src``
by your true module name. You also need to replace ``python3_module_template`` wherever it is found:

* ``project_var_name  = 'python3_module_template'`` in ``setup.py``, ``make_help.py`` and ``_doc/sphinxdoc/source/conf.py``
* ``from src.python3_module_template.subproject.myexample import myclass`` in ``_unittests/ut_example/test_example.py``
* many places in ``_doc/sphinxdoc/source/index.rst``
* many places in ``README.rst``

Automation
----------

* `Generating the setup with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/contribute.html?generate-the-setup#generate-the-setup>`_
* `Generating the documention with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/contribute.html?generate-the-setup#documentation>`_
* `Installation <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/contribute.html?generate-the-setup#installation>`_
* `Unit tests with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/doctestunit.html>`_

Adding a new module or subpackage
+++++++++++++++++++++++++++++++++

Any new module or subpackage should be added in ``src/python3_module_template``. Every subfolder should
contain a file ``__init__.py``. If the new file needs an existing submodule, you need
to add something like the following::

    import os
    import sys

    from ..subproject.myexample import myclass

You must use relative imports.
To add a module at deeper level than the previous one, you
should add relative imports in every ``__init__.py`` along the way.
