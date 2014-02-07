"""

This the documentation of this module.

"""
import os,sys


# replace # from ..subproject.myexample import myclass
import sys,os
path=os.path.normpath(os.path.join(os.path.abspath(os.path.split(__file__)[0]),'..'))
sys.path.insert(0,path)
from subproject.myexample import myclass
del sys.path[0]

class myclass2 (myclass) :
    """


This is the documentation for this class.

+------------+------------------------------+
| attribute  | meaning                      |
+============+==============================+
| pa         | an example of an attribute.  |
+------------+------------------------------+



    """
    
    def __init__ (self, pa) :
        """
        
                documentation for the constructor

                :param      pa:      first parameter
                
        """
        self.pa = pa
        
    def get_value(self, mul) :
        """
        
                returns the parameter multiplied by a value

                :param      mul:     a float
                :return:             a float
                
        """
        return self.pa * mul
        
    @staticmethod
    def static_example():
        """
        
                :return: a boolean
                
        """
        return True
        
    @property
    def property_example(self):
        """
        
                a property example
                
        """
        return True
        
        