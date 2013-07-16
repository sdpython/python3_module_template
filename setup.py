# coding: utf-8

#  Copyright (C) 2013 ---------------
#  All rights reserved.
# 
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
# 
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
# 
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
# 
#  3. All advertising materials mentioning features or use of this
#     software must display the following acknowledgment:
#     "This product includes software developed by
#      --------------- <--------------- AT --------------->"
# 
#  4. Redistributions of any form whatsoever must retain the following
#     acknowledgment:
#     "This product includes software developed by
#      --------------- <--------------- AT --------------->."
# 
#  THIS SOFTWARE IS PROVIDED BY --------------- ``AS IS'' AND ANY
#  EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL Roman V. Kiseliov OR
#  ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
#  OF THE POSSIBILITY OF SUCH DAMAGE.

# http://docs.python.org/3.3/install/index.html
# http://docs.python.org/3.3/distutils/sourcedist.html
# http://docs.python.org/3.3/distutils/setupscript.html#setup-script

__rev_id__ = """setup.py,v 1.0 01/12/2009"""

import sys,os, re, zipfile

project_var_name    = "project_name"
sversion            = "0.1"
versionPython       = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path                = "Lib/site-packages/" + project_var_name
subversion          = 1   

KEYWORDS = \
project_var_name + ', first name, last name'

DESCRIPTION = \
"""This a project template including a setup and the generation of sphinx generation."""

CLASSIFIERS = \
[
'Development Status :: ' + sversion + ' - Alpha',
'Operating System :: any',
'Programming Language :: Python and C++',
'License :: GNU 2.0',
'Development Status :: __VERSION__',
'Intended Audience :: Developers',
'Topic :: SQL :: XML :: MATRIX :: TABLE :: GRAPH',
'Programming Language :: Python',
'Intended Audience :: Developers',
'License :: Python Software Foundation License',
'Topic :: Helpers :: GNUPlot :: ENSAE',
'Python 3.3 :: Windows :: Linux',
]

# dirname is not used by sdist.py
data_files  = [ 
                (os.path.join(path, "subproject"), 
                    [ "src/" + project_var_name + "/subproject/myexample_nouse.tohelp" ]
                ),
            ]
                    
if "bdist_wininst" in sys.argv :
    # for the windows setup, we add other files if needed
    data_files += [ 
                    #(os.path.join(path, "subproject"), 
                    #        ["src/" + project_var_name + "/subproject/file.pyd",
                    #    ] ),
                    ]
    

#############################################################
# begin checking
#############################################################

def remove_existing_build_setup() :
    if "bdist_wininst" not in sys.argv :
        for p in ["dist", "src/dist"] :
            if os.path.exists (p) :
                for exe in os.listdir (p) :
                    if ".exe" in exe or ".zip" in exe or ".gz" in exe :
                        print ("removing ", exe)
                        os.remove (os.path.join(p, exe))

remove_existing_build_setup()

#############################################################
# end checking
#############################################################



#import distutils.sysconfig as SH
from setuptools import setup, find_packages, Extension


if "bdist_wininst" not in sys.argv :
    EXT_MODULES = [ 
                    #Extension(project_var_name + '.subproject.sample_module', 
                    #    ['src/' + project_var_name + '/subproject/sample_module.cpp'], 
                    #    include_dirs = ['src/' + project_var_name + '/subproject']),
                ]
else :
    EXT_MODULES = [ ]


packages        = find_packages ()
package_dir     = { k : k.replace(".","/") for k in packages }
readme          = 'README.rst'
with open(readme) as f : long_description = f.read()


setup(
    name                    = project_var_name,
    version                 = 'v%s.%d' % (sversion, subversion),
    author                  = 'author',
    author_email            = 'author AT something.any',
    url                     = "http://...",
    download_url            = "https://github.com/...",
    description             = DESCRIPTION,
    long_description        = long_description,
    keywords                = KEYWORDS,
    classifiers             = CLASSIFIERS,
    packages                = find_packages('src', exclude='src'),
    package_dir             = { '': 'src' },
    data_files              = data_files,
    requires                = [  
                                # "numpy (>= 1.7.1)",
                                ],
    ext_modules             = EXT_MODULES
    )
    
    