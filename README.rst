.. _l-README:

README
======


**Links:**
    * `GitHub/python_project_template <https://github.com/sdpython/python_project_template/>`_
    * `documentation <http://www.xavierdupre.fr/site2013/index_code.html#python_project_template>`_



Introduction
------------

This project is a skeleton for any new project. It contains:
   * a source folder: ``src``
   * a unit test folder: ``_unittests``, go to this folder and run ``run_unittests.py``
   * a _doc folder: ``_doc``, it will contains the documentation
   * a file ``setup.py`` to build and to install the module
    
All theses steps were only tested on Windows. Suppot for linux will be added later. To create your own project, you need to rename the folder ``project_name`` in ``src`` by your true module name. You also need to replace ``project_name`` wherever it is found:
   * ``project_var_name  = 'project_name'`` in ``setup.py``, ``make_help.py`` and ``_doc/sphinxdoc/source/conf.py``
   * ``from src.project_name.subproject.myexample import myclass`` in ``_unittests/ut_example/test_example.py``
   * many places in ``_doc/sphinxdoc/source/index.rst``
   * many places in ``README.rst``
    
The project is also hosted `here <http://www.xavierdupre.fr/site2013/index_code.html>`_ 
where you can find a 
`link <http://www.xavierdupre.fr/app/python_project_template/helpsphinx/index.html>`_ 
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

* **0.0 - 2014/??/??**
    * **new:** first version
    