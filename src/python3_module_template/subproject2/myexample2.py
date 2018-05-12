"""
@file
@brief This the documentation of this module (myexample2).

To make a reference to a blog post, just read :ref:`label-to-this-blogpost`.

The following documentation comes from a directive
`runpython
<http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/helpgen/sphinx_runpython_extension.html>`_
which outputs documentation on the standard output::

    .. runpython::
        :showcode:

        for l in range(0,10):
            print("    line", l)

Which gives:

.. runpython::
    :showcode:

    for l in range(0,10):
        print("    line", l)

And without the input code:

.. runpython::

    for l in range(0,10):
        print("    line", l)

You can also add option *rst*::

    .. runpython::
        :rst:

        for l in range(0,10):
            print("**line**", "*" +str(l)+"*")
            print('')

Which displays interpreted RST:

.. runpython::
    :rst:

    for l in range(0,10):
        print("**line**", "*" +str(l)+"*")
        print('')

It can be run in a separate process with option ``:process:``
(click on source):

.. runpython::
    :process:

    import python3_module_template
    import os
    print(os.path.split(python3_module_template.__file__)[-1])
"""
from ..subproject.myexample import myclass


class myclass2(myclass):

    """
    This is the documentation for this class.

    @var   pa   an example of an attribute.

    Inline :math:`x^2 + y + z`. Another equation to test:

    .. math::

        x^2 + y

    .. math::

        \\sum_{i=1}^n x^2

    """

    def __init__(self, pa):
        """
        @param      pa      first parameter
        """
        myclass.__init__(self, pa)

    def get_value(self, mul):
        """
        returns the parameter multiplied by a value
        @param      mul     a float
        @return             a float
        """
        return self.pa * mul

    @staticmethod
    def static_example():
        """
        @return a boolean
        """
        return True

    @property
    def property_example(self):
        """
        a property example
        """
        return True
