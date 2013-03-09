import doctest
from interlude import interact
from pprint import pprint
import re
import unittest
import zc.buildout.tests
import zc.buildout.testing
from zope.testing import renormalizing

TESTFILES = [
    'sdk.rst',
]
optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE


def setUp(test):
    zc.buildout.tests.easy_install_SetUp(test)
    zc.buildout.testing.install('hexagonit.recipe.download', test)
    zc.buildout.testing.install_develop('collective.recipe.appengine', test)


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            filename,
            setUp=setUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint},
            checker=renormalizing.RENormalizing([
                    zc.buildout.testing.normalize_path,
                    (re.compile(r'http://localhost:\d+'),
                                'http://test.server'),
                    # Clean up the variable hashed filenames to avoid spurious
                    # test failures
                    (re.compile(r'[a-f0-9]{32}'), ''),
                    ]),
        ) for filename in TESTFILES
    ])


if __name__ == '__main__':  # pragma NO COVERAGE
    unittest.main(defaultTest='test_suite')  # pragma NO COVERAGE
