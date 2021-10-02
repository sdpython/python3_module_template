# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass

#########
# settings
#########

project_var_name = "python3_module_template"
project_owner = "sdpython"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = 'HISTORY.rst'

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


here = os.path.dirname(__file__)
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}
package_data = {project_var_name + ".subproject": ["*.tohelp"]}


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name),
    author='author',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://...",
    download_url="https://github.com/sdpython/%s/" % project_var_name,
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=['pyquicksetup>=0.2'],
)
