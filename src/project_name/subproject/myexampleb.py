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

    """

    def __init__(self, pa):
        """
        documentation for the constructor
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
        return v1 + v2
