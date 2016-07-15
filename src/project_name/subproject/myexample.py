# -*- coding: utf-8 -*-
"""
@file
@brief This the documentation of this module (myexampleb).
"""


class myclass:

    """
    This is the documentation for this class.

    @example(an example of use)
    Just for documentation purpose.
    @code
    m = myclass(0)
    @endcode
    @endexample

    **FAQ**

    .. faqref::
        :title: How to add a question ?

        Just look a this section.
        Look also :ref:`l-FAQ2`.

    **BLOC**

    .. blocref::
        :title: How to add a bloc
        :tag: aaaa

        Just look a this bloc.
        Look also :ref:`l-FAQ2`.

    An accent, é, to check it is working.
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
