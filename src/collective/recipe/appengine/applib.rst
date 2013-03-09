Create minimal buildout::

    >>> write(sample_buildout, 'buildout.cfg',
    ... """
    ... [buildout]
    ... newest = false
    ... parts = gaeapplib
    ...
    ... [gaeapplib]
    ... recipe = collective.recipe.appengine:applib
    ... lib-directory = distlib
    ... use-zipimport = false
    ... eggs = 
    ...     interlude
    ... # Don't install these packages or modules.
    ... ignore-packages =
    ...     distribute
    ... """)
    
Run buildout::

    >>> print(system(buildout))
    Installing gaeapplib.
    gaeapplib: Library not installed: missing egg info for '/sample-buildout/eggs/distribute-0.6.35-py2.7.egg'.
    gaeapplib: Copying '/sample-buildout/eggs/interlude-1.1.1-py2.7.egg/interlude'...
    <BLANKLINE>

    
Is it there?

::

    >>> ls(sample_buildout, 'distlib')
    -  ATTENTION_DO_NOT_EDIT_IN_HERE.txt
    d  interlude    