"""
@file
@brief This the documentation of this module (myexample2).


The following documentation comes from a directive ``runpython``
which outputs documentation on the standard output::

    print("::")
    for l in range(0,10):
        print("    line", l)

Which gives:

.. runpython::
    :indent: 0

    print("::")
    for l in range(0,10):
        print("    line", l)

"""
from ..subproject.myexample import myclass


class myclass2 (myclass):

    """
    This is the documentation for this class.

    @var   pa   an example of an attribute.
    """

    def __init__(self, pa):
        """
        documentation for the constructor
        @param      pa      first parameter
        """
        self.pa = pa

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
