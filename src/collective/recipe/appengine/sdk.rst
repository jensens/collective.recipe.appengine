::
    >>> import os.path
    >>> testdata = join(os.path.dirname(__file__), 'testdata')
    >>> server = start_server(testdata)
    >>> mkdir(sample_buildout, 'downloads')

In the simplest form we can download a simple package and have it
extracted in the parts directory::

    >>> write(sample_buildout, 'buildout.cfg',
    ... """
    ... [buildout]
    ... newest = false
    ... parts = gaesdk
    ...
    ... [gaesdk]
    ... recipe = collective.recipe.appengine:sdk
    ... url = %spackage1-1.2.3-final.tar.gz
    ... """ % server)

Ok, let's run the buildout::

    >>> print(system(buildout))
    Installing gaesdk.
    Downloading http://test.server/package1-1.2.3-final.tar.gz
    gaesdk: Extracting package to /sample-buildout/parts/gaesdk
    <BLANKLINE>
    
Let's take a look at the buildout parts directory now::

    >>> ls(sample_buildout, 'parts')
    d gaesdk
