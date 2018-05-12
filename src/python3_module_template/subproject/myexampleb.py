"""
@file
@brief This the documentation of this module (myexampleb).
"""

from .myexample import myclass


class myclassb(myclass):

    """
    This is the documentation for this class.
    Inherits from @see cl myclass.
    An example on how to share: :sharenet:`facebook-linkedin-twitter-20-body`.

    .. todoext::
        :title: An example of a todo
        :tag: enhancement
        :issue: 1
        :index: todoext example

        Check the documentation to see how it is rendered.
    """

    def __init__(self, pa):
        """
        @param      pa      first parameter
        """
        myclass.__init__(self, pa)

    def method_napoleon(self, v1, v2):
        """
        Example of a docstring used by *sphinx.ext.napoleon* extension.

        Args:
            v1 (int): a integer
            v2 (float): a float

        Returns:
            float: the sum

        Raises:
            TypeError: for a type mismatch

        See `google style <http://sphinx-doc.org/ext/example_google.html#example-google>`_
        """
        return self.pa + v1 + v2


def onefunction(a, b):
    """
    Returns the addition of ``a+b``.

    :param a: first element
    :param b: second element
    :return: ``a + b``
    :raises TypeError: if a and b have different types.
    """
    if type(a) != type(b):
        raise TypeError("Different type {0} != {1}".format(a, b))
    return a + b
