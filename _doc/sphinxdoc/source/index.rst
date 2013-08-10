.. project_name documentation documentation master file, created by
   sphinx-quickstart on Fri May 10 18:35:14 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PROJECT_NAME documentation
=====================================

.. contents::
   :depth: 3


Introduction
------------

This project is a template to start a new project. See :ref:`l-README`.
    
Installation 
------------


* Windows installation: 
    * run the setup ``project_name*.win32.exe``
* Windows installation with source:
    * download the file ``project_name*.tar.gz`` and unzip it
    * type the following commands::
    
        set PATH=%PATH%;c:\Python33
        python.exe setup.py install    
        
* Linux installation:
    * download the file ``project_name*.tar.gz``
    * type the following commands::
    
        tar xf project_name-py3.3.tar.gz
        sudo su
        python3.3 setup.py install
        
* Using pip::

    pip install project_name


You can check the module is working for basic functions by running::
    
    import project_name
    project_name.check()
    
        
Quick overview
--------------

* **Example**
    * example:  :class:`myclass <subproject.myexample.myclass>`

See :ref:`l-usecase`.

Changes
-------

* :ref:`l-changes`

About this documentation
------------------------

.. toctree::
    :maxdepth: 2

    generatedoc
    glossary
    confr_pyp

    
Indices and tables
==================

* :ref:`l-modules`
* :ref:`ext-tohelp`
* :ref:`l-functions`
* :ref:`l-classes`
* :ref:`l-methods`
* :ref:`l-staticmethods`
* :ref:`l-properties`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
   

