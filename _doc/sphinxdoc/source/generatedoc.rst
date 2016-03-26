Generate this documentation
===========================


.. generatedoc:

See `Generating the documention with pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/generatedoc.html>`_.


Configuration:

.. literalinclude:: conf.py
 
 
Extensions to install
+++++++++++++++++++++

* `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper/>`_
* `wild_sphinx_theme <https://pypi.python.org/pypi/wild_sphinx_theme>`_

Tips
++++

Module `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper/>`_
defines sphinx command 
`runpython <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/helpgen/sphinx_runpython_extension.html>`_
which generates from a python script included in the documentation itself. 
The following snippet produces a table.

.. runpython::
    :rst:
    :showcode:
    
    from pyquickhelper.pandashelper import df2rst
    import pandas
    df = pandas.DataFrame([{"x": 3, "y":4}, {"x": 3.5, "y":5}])
    print(df2rst(df))

The next one is more complex. The code produces titles,
label and references. It requires Sphinx engine to be processed.

.. runpython::
    :rst:
    :showcode:
    :showout:

    rows = []
    list_title = ["T1", "T2", "T3"]
    back = None
    for t in list_title:
        rows.append("")
        rows.append(".. _l-fake_title-" + t + ":")
        rows.append("")
        rows.append(t*3)
        rows.append("^" * len(t*3))
        rows.append("")
        if back:
            rows.append("link :ref:`l-fake_title-" + back + "`")
        else:
            rows.append("no link")
        rows.append("")
        back = t
    print("\n".join(rows))
