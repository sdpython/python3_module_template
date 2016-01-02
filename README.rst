
.. _l-README:

README / Changes
================

.. image:: https://travis-ci.org/sdpython/python3_module_template.svg?branch=master
    :target: https://travis-ci.org/sdpython/python3_module_template
    :alt: Build status
    
.. image:: https://ci.appveyor.com/api/projects/status/6qp50sxl22aqwtb5?svg=true
    :target: https://ci.appveyor.com/project/sdpython/python3_module_template
    :alt: Build Status Windows
    
.. image:: https://badge.fury.io/py/project_name.svg
    :target: http://badge.fury.io/py/project_name    

.. image:: http://img.shields.io/pypi/dm/project_name.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/project_name

.. image:: http://img.shields.io/github/issues/sdpython/python3_module_template.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/python3_module_template/issues
    
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT
    
.. image:: https://coveralls.io/repos/sdpython/python3_module_template/badge.svg?branch=master&service=github 
    :target: https://coveralls.io/github/sdpython/python3_module_template?branch=master     

.. image:: https://landscape.io/github/sdpython/python3_module_template/master/landscape.svg?style=flat
   :target: https://landscape.io/github/sdpython/python3_module_template/master
   :alt: Code Health
   
.. image:: https://requires.io/github/sdpython/python3_module_template/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/python3_module_template/requirements/?branch=master
     :alt: Requirements Status   
    
.. image:: https://codecov.io/github/codecov/python3_module_template/coverage.svg?branch=master
    :target: https://codecov.io/github/codecov/python3_module_template?branch=master
    
      

**Links:**
    * `GitHub/python3_module_template <https://github.com/sdpython/python3_module_template/>`_
    * `documentation <http://www.xavierdupre.fr/site2013/index_code.html#python3_module_template>`_
    * `Travis <https://travis-ci.org/sdpython/python3_module_template>`_
    * `Blog <http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/blog/main_0000.html#ap-main-0>`_



Introduction
------------

This project is a skeleton for any new project. It contains:

* a source folder: ``src``
* a unit test folder: ``_unittests``, go to this folder and run ``run_unittests.py``
* a _doc folder: ``_doc``, it will contains the documentation
* a file ``setup.py`` to build and to install the module
    
All theses steps were only tested on Windows. Suppot for linux will be added later. 
To create your own project, you need to rename the folder ``project_name`` in ``src`` 
by your true module name. You also need to replace ``project_name`` wherever it is found:

* ``project_var_name  = 'project_name'`` in ``setup.py``, ``make_help.py`` and ``_doc/sphinxdoc/source/conf.py``
* ``from src.project_name.subproject.myexample import myclass`` in ``_unittests/ut_example/test_example.py``
* many places in ``_doc/sphinxdoc/source/index.rst``
* many places in ``README.rst``
    
The project is also hosted `here <http://www.xavierdupre.fr/site2013/index_code.html>`_ 
where you can find a 
`link <http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/index.html>`_ 
to the generated documentation based on this template.
    
Automation
----------

* `Generating the setup with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/generatesetup.html>`_
* `Generating the documention with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/generatedoc.html>`_
* `Installation <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/installation.html>`_
* `Unit tests with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/doctestunit.html>`_

Adding a new module or subpackage
+++++++++++++++++++++++++++++++++

Any new module or subpackage should be added in ``src/project_name``. Every subfolder should
contain a file ``__init__.py``. If the new file needs an existing submodule, you need
to add something like the following::

    import os,sys

    from ..subproject.myexample import myclass
    
You should use relative imports as much as possible.
To add a module at deeper level than the previous one, you
should add relative imports in every ``__init__.py`` along the way.


Versions
--------

* **0.1 - 2016/??/??**
    * **new:** first version
    * **fix:** the setup does not need the file ``README.rst`` anymore
    * **add:** unit test to check the file ``README.rst`` follows the syntax of docutils 0.8 (for pipy)
    * **add:** add a unit test to run all notebooks offlines
    