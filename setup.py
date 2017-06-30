# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "project_name"
sversion = "0.2"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'


KEYWORDS = project_var_name + ', first name, last name'
DESCRIPTION = "This a project template including a setup and the generation of sphinx " + \
              "generation. The documentation generation and the unit test are using pyquickhelper."


CLASSIFIERS = [
    'Programming Language :: Python :: %d' % sys.version_info[0],
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]


#######
# data
#######


packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".subproject": ["*.tohelp"]}

############
# functions
############


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    from pyquickhelper.pycode.setup_helper import available_commands_list
    return available_commands_list(sys.argv)


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and "--help" not in sys.argv and "--help-commands" not in sys.argv:
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    if sys.version_info[0] != 2:
        write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Subversion is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion:
    # avoid uploading with a wrong subversion number
    try:
        import pyquickhelper
        pyq = True
    except ImportError:
        pyq = False
    raise Exception(
        "subversion is empty, cannot upload, is_local()={0}, pyquickhelper={1}".format(is_local(), pyq))

##############
# common part
##############

if os.path.exists(readme):
    if sys.version_info[0] == 2:
        from codecs import open
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""

if "--verbose" in sys.argv:
    verbose()

if is_local():
    from pyquickhelper import get_fLOG
    logging_function = get_fLOG()
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function(OutputPrint=True)
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        extra_ext=["tohelp"],
        add_htmlhelp=sys.platform.startswith("win"),
        coverage_options=dict(omit=["*exclude*.py"]),
        fLOG=logging_function, covtoken=(
            "ce1fc48d-9081-44b3-ae09-8b4665e28e86", "'_UT_36_std' in outfile"),
        layout=["pdf", "epub", "html",
                ("html", "build2", {"html_theme": "alabaster"}, "source/phdoc_static2")])
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)

    setup(
        name=project_var_name,
        version='%s%s' % (sversion, subversion),
        author='author',
        author_email='author@something.any',
        url="http://...",
        download_url="https://github.com/.../",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        # data_files=data_files,
        # install_requires=['numpy', 'ipython'],
        # include_package_data=True,
    )
