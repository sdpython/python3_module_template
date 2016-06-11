

.. blogpost::
    :title: Make a reference to a blog post
    :keywords: reference, blog, post
    :date: 2016-06-11
    :categories: documentation
    :lid: label-to-this-blogpost
    
    Option ``lid`` to the directive ``blogpost`` 
    to specify a label. The documentation can now refer to it.
    
    ::
    
        .. blogpost::
            :title: Make a reference to a blog post
            :keywords: reference, blog, post
            :date: 2016-06-11
            :categories: documentation
            :lid: label-to-this-blogpost
            
    And to add a link:
    
    ::
    
        :ref:`label-to-this-blogpost` 
