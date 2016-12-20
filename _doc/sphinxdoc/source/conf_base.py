import wild_sphinx_theme

try:
    from pyquickhelper.helpgen.default_conf import set_sphinx_variables
except ImportError as e:
    import os
    import sys
    paths = "\n".join(sys.path)
    raise ImportError("pyquickhelper is not installed. PYTHONPATH={0}\nsys.path=\n{1}".format(
        os.environ.get("PYTHONPATH", None), paths))
set_sphinx_variables(__file__, "project_name", "author(s)", 2016,
                     "wild", wild_sphinx_theme.get_theme_dir(), locals(),
                     extlinks=dict(issue=('https://github.com/sdpython/python3_module_template/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"


def custom_latex_processing(latex):
    """
    process a latex file and returned the modified version
    
    @param      latex       string
    @return                 string
    """
    print("******", len(latex))
    stop
    if latex is None:
        raise ValueError("Latex is null")
    # this weird modification is only needed when jenkins run a unit test in pyquickhelper (pycode)
    return latex.replace("gynotebooks\\Python_logo_and_wordmark", "Python_logo_and_wordmark")
