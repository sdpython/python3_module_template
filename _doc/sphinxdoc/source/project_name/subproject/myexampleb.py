"""

This the documentation of this module.

"""


# replace # from .myexample import myclass
import sys,os
path=os.path.normpath(os.path.join(os.path.abspath(os.path.split(__file__)[0])))
sys.path.insert(0,path)
from myexample import myclass
del sys.path[0]

class myclassb(myclass) :
    """
    
        This is the documentation for this class.
        
        see :class:`myclass <subproject.myexample.myclass>`
        
    """
    
    def __init__ (self, pa) :
        """
        
                documentation for the constructor

                :param      pa:      first parameter
                
        """
        myclass.__init__(self, pa)
