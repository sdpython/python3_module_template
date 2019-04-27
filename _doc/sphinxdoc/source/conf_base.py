import sphinx_gallery
import sphinx_rtd_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
try:
    import python3_module_template
except ModuleNotFoundError:
    raise ModuleNotFoundError("Cannot import python3_module_template\n{}".format(
        "\n".join(sys.path)))


set_sphinx_variables(__file__, "python3_module_template", "sdpython", 2019,
                     "sphinx_rtd_theme", [
                         sphinx_rtd_theme.get_html_theme_path()],
                     locals(), book=True,
                     extlinks=dict(issue=('https://github.com/sdpython/python3_module_template/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet(),
}

nblinks = {'slideshowrst': 'http://www.xavierdupre.fr/'}


def custom_latex_processing(latex):
    """
    process a latex file and returned the modified version

    @param      latex       string
    @return                 string
    """
    if latex is None:
        raise ValueError("Latex is null")
    # this weird modification is only needed when jenkins run a unit test in
    # pyquickhelper (pycode)
    return latex
