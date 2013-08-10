"""
This the documentation of this module.
"""

from .myexample import myclass

class myclassb(myclass) :
    """
    This is the documentation for this class.
    
    @see cl myclass
    """
    
    def __init__ (self, pa) :
        """
        documentation for the constructor
        @param      pa      first parameter
        """
        myclass.__init__(self, pa)
