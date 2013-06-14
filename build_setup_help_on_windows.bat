IF EXIST c:\python33vir\virt2\Scripts (
    set pythonexe="c:\python33vir\virt2\Scripts\python"
) ELSE (
    set pythonexe="c:\python33\python"
)
%pythonexe% setup.py sdist --formats=gztar,zip
%pythonexe% setup.py bdist_wininst
%pythonexe% make_help.py
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html

rem we open a browser with on the generated help
dist\html\index.html

