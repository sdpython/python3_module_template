"""

This the documentation of this module.

"""

class myclass :
    """
    
        This is the documentation for this class.
        
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
        
        