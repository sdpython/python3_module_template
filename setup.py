# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass
from pyquicksetup.pyquick import SetupCommandSphinx

#########
# settings
#########

project_var_name = "python3_module_template"
project_owner = "sdpython"
versionPython = f"{sys.version_info.major}.{sys.version_info.minor}"
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = 'HISTORY.rst'

KEYWORDS = [project_var_name, 'first name, last name']
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


class MySetupCommandSphinx(SetupCommandSphinx):
    description = "Builds documentation."

    user_options = [
        ('layout=', None, 'format generation, default is html,rst.'),
        ('nbformats=', None,
         'format generation, default is ipynb,slides,html,python,rst,github'),
    ]

    def initialize_options(self):
        self.layout = "html,rst"
        self.nbformats = "ipynb,slides,html,python,rst,github"

    def run(self):
        from pyquickhelper.pycode import process_standard_options_for_setup
        parameters = self.get_parameters()
        parameters['argv'] = ['build_sphinx']
        parameters['layout'] = self.layout.split(',')
        parameters['nbformats'] = self.nbformats.split(',')
        process_standard_options_for_setup(**parameters)


cmdclass = default_cmdclass()
cmdclass['build_sphinx'] = MySetupCommandSphinx


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name),
    author='author',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://...",
    download_url=f"https://github.com/sdpython/{project_var_name}/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=cmdclass,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=['pyquicksetup>=0.2'],
)
