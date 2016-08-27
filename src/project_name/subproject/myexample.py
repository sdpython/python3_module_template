# -*- coding: utf-8 -*-
"""
@file
@brief This the documentation of this module (myexampleb).
"""


class myclass:

    """
    This is the documentation for this class.

    **example with a sphinx directives**

    It works everywhere in the documentation.

    .. exref::
        :title: an example of use

        Just for documentation purpose.

        ::

            m = myclass(0)

    The old way:

    @example(an old example of use)

    This only works from the code,
    not inserted in a RST file. The source
    documentation is parsed and every such example is
    collected and placed in a page ``all_examples.rst``
    (look at the source).

    @code
    m = myclass(0)
    @endcode

    @endexample

    **FAQ**

    .. faqref::
        :title: How to add a question ?

        Just look a this section.
        Look also :ref:`l-FAQ2`.

    .. faqref::
        :title: Add a label
        :lid: label1

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
