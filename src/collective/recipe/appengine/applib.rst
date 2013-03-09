Create minimal buildout::

    >>> write(sample_buildout, 'buildout.cfg',
    ... """
    ... [buildout]
    ... newest = false
    ... parts = gaeapplib
    ...
    ... [gaeapplib]
    ... recipe = collective.recipe.appengine:applib
    ... lib-directory = ${buildout:distlib-directory}
    ... use-zipimport = false
    ... eggs = 
    ...     webtest
    ... """ % server)