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

project_var_name = "project_name"

def get_svn_version (path = ".") :
    try :
        import pysvn
        svnClient   = pysvn.Client()
        info        = svnClient.info2(".")
        infos       = [_[1] for _ in info ]
        revv        = [ _["rev"].number for _ in infos]
        revision    = max(revv)
        with open("version.txt", "w") as f : f.write("%d" % revision)
        return revision
    except ImportError as e : 
        with open("version.txt", "r") as f :
            return int(f.read().strip(" \n\r\t"))
    except Exception as e :
        if "is not a working copy" in str(e) :
            with open("version.txt", "r") as f :
                return int(f.read().strip(" \n\r\t"))
        else :
            raise e
        

if len(sys.argv) == 1 and sys.argv[0] == "setup.py" :
    try :
        svn = get_svn_version()
    except Exception as e:
        svn = "unknown"
    print ("SVN latest version ", svn)


def ishome () :
    return True or len(sys.argv) > 1 and sys.argv[1] in ["sdist", "bdist_wininst"]
    
def install() :
    return "install" in sys.argv

#############################################################
# extra foldders
#############################################################
                
def get_folder_files (folder, excludePyFile = False, svn = False, recursive = False) :
           
    svn = svn and not install()
    
    if os.path.exists (folder) : 
        if svn :
            try :
                import pysvn
                svnClient = pysvn.Client()
                li      = svnClient.ls (folder)
            except Exception as e :
                if "is not a working copy" in str(e) :
                    svn = False
                
        if svn :
            import pysvn
            svnClient = pysvn.Client()
            li      = svnClient.ls (folder)
            files   = [ _.name for _ in li if os.path.isfile(_.name) ]
            if recursive : 
                folders = [ _.name for _ in li if os.path.isdir(_.name) ]
                while len (folders) > 0 :
                    f  = folders.pop()
                    li = svnClient.ls (f)
                    f  = [ _.name for _ in li if os.path.isfile(_.name) ]
                    if len(f) > 0 : files.extend(f)
                    f  = [ _.name for _ in li if os.path.isdir(_.name) ]
                    if len(f) > 0 : folders.extend(f)
                
        else :
            folders = [ os.path.join(folder, _) for _ in os.listdir (folder) ]
            files   = folders
            if recursive : 
                folders = [ _ for _ in files if os.path.isdir(_) ]
                while len (folders) > 0 :
                    f  = folders.pop()
                    f  = [ os.path.join(f, _) for _ in os.listdir (f) ]
                    if len(f) > 0 : files.extend(f)
                    f  = [ _  for _ in f if os.path.isdir(_) ]
                    if len(f) > 0 : folders.extend(f)
            files = [ _ for _ in files if os.path.isfile(_) ]
        if excludePyFile :
            files = [ _ for _ in files if not _.endswith(".py") ]
        if len(files) == 0 : 
            raise Exception("there should be at least one file in folder: " + folder)
            
        files = [ _ for _ in files if "\\build\\" not in _ and \
                                      "/build/" not in _ and  \
                                      "__pycache__" not in _ ]
        return files
    elif ishome() :
        raise Exception("folder " + folder + " is missing")
    else :
        return []
        

# dirname is not used by sdist.py
path = "Lib/site-packages/" + project_var_name
data_files  = [ 
                #(os.path.join(path, project_var_name, "subproject"), 
                #            get_folder_files("src/" + project_var_name + "/subproject", svn = True, recursive = False) ),
                    ]
                    
if "bdist_wininst" in sys.argv :
    # for the windows setup, we add the compiled files
    data_files += [ 
                    #(os.path.join(path, project_var_name + "/subproject"), 
                    #        ["src/" + project_var_name + "/subproject/file.pyd",
                    #    ] ),
                    ]
    

#############################################################
# begin checking
#############################################################

versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)

        
def check_modules () :
    modules_to_check = ["numpy" ]
    notPresent = [ ]
    for mod in modules_to_check :
        st = "import %s" % mod
        try :
            exec (st)
        except ImportError :
            notPresent.append (mod)
    if len(notPresent) > 0 :
        raise ImportError ("following modules should be installed: %s" % ", ".join(notPresent))

def remove_existing_build_setup() :
    if "bdist_wininst" not in sys.argv :
        if os.path.exists ("dist") :
            for exe in os.listdir ("dist") :
                if ".exe" in exe or ".zip" in exe or ".gz" in exe :
                    print ("removing ", exe)
                    os.remove (os.path.join("dist", exe))

def check_pathes() :
    if True or ishome() :
        missing = [ ]
        all     = [ ]
        for row in data_files :
            path,folders = row[0], row[-1]
            for f in folders :
                if not os.path.exists (f) :
                    missing.append (f)
                all.append(f)
        if len(missing) > 0 :
            raise Exception ("following folders should be present:\n%s" % "\n".join(missing))

def find_packages () :
    from pyhome3.srcpyhome.core.file.folder import explore_folder
    folders,allfiles = explore_folder ("src", project_var_name, True)
    if len(allfiles) == 0 :
        raise Exception("unable to find any packages in " + os.path.abspath(os.path.join("src", project_var_name)))

    folders = [ _ for _ in folders if   "\\build" not in _  and \
                                        "/build" not in _ and \
                                          "__pycache__" not in _ and \
                                          "_doc\\sphinxdoc" not in _ and \
                                          "_doc/sphinxdoc" not in _ ]
                                        
    folders = [ _.replace("\\",".").replace("/",".") for _ in folders ]
    folders = { _:0 for _ in folders }
    folders = list(folders.keys())
    folders.sort()
    return folders

check_modules()
check_pathes()
remove_existing_build_setup()

#############################################################
# end checking
#############################################################




DESCRIPTION = \
"""This module gathers various precesses I use at home or for my teachings
to automate some  tasks (such as updating my website, comparing folders, playing with 
tables, sqlite3, graphviz, imagemagick, xml, ...)"""

CLASSIFIERS = \
[
'Development Status :: 0.5 - Alpha',
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



from distutils.core import setup, Extension
import distutils.sysconfig as SH



if "bdist_wininst" not in sys.argv :
    EXT_MODULES = [ 
                    #Extension(project_var_name + '.subproject.sample_module', 
                    #    ['src/' + project_var_name + '/subproject/sample_module.cpp'], 
                    #    include_dirs = ['src/' + project_var_name + '/subproject']),
                ]
else :
    EXT_MODULES = [ ]


KEYWORDS = \
project_var_name + ', first name, last name'


packages                = find_packages ()
package_dir             = { k : k.replace(".","/") for k in packages }

if os.path.exists ("src") :
    os.chdir ("src")
    back = True
    
    packages        = [ _.replace ("src.","") for _ in packages ]
    package_dir     = { k : k.replace(".","/") for k in packages }
    readme          = '../README.rst'
else :
    back = False    
    readme = 'README.rst'



setup(
    name                    = project_var_name + '-py' + versionPython,
    version                 = 'v0.5.%d' % get_svn_version (),
    author                  = 'author',
    author_email            = 'author AT something.any',
    url                     = "http://...",
    download_url            = "http://...",
    description             = DESCRIPTION,
    long_description        = open(readme).read(),
    keywords                = KEYWORDS,
    classifiers             = CLASSIFIERS,
    packages                = packages,
    package_dir             = package_dir,
    data_files              = data_files,
    requires                = [  
                                # "numpy (>= 1.7.1)",
                                ],
    ext_modules             = EXT_MODULES,
    include_package_data    = True
    )
    
if back :
    os.chdir("..")
    if not os.path.exists ("dist") :
        os.mkdir ("dist")
    os.system("copy /Y src\\dist\\*.* dist")
    os.system("rmdir /S /Q src\\dist")
    os.system("rmdir /S /Q src\\build")
    
if "install" in sys.argv :
    # we check the data was installed
    import shutil
    site_pack = [ _ for _ in sys.path if _.endswith("site-packages") ][0]
    lookup    = os.path.join(site_pack, "_doc", "sphinx", "source", "project_ico.ico")
    if not os.path.exists (lookup) :
        # we have issues
        for fold, files in data_files :
            fol_ = fold[fold.find("site-packages") + len("site-packages"):].lstrip("/\\")
            dest = os.path.join(site_pack, fol_)
            if not os.path.exists (dest) : 
                print ("create folder ", dest)
                os.makedirs(dest)
            for f in files :
                print ("copy file ", f, " to ", dest)
                shutil.copy (f, dest)
      
if ishome() and sys.argv[1] == "sdist" :
    dist = os.listdir ("dist")
    zip  = [ _ for _ in dist if ".zip" in _ ]
    if len(zip) != 1 : raise Exception("no zip file was found in dist foler")
            
