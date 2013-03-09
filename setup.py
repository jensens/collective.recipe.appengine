import os
from setuptools import setup, find_packages

version = '1.0RC1'
short_description = 'Buildout recipes for App Engine development.'


def get_readme():
    base = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
    files = [
        os.path.join(base, 'README.rst'),
        os.path.join(base, 'CHANGES.rst'),
    ]
    content = []
    for filename in files:
        f = open(filename, 'r')
        content.append(f.read().strip())
        f.close()

    return '\n\n\n'.join(content)

setup(
    name='collective.recipe.appengine',
    version=version,
    description=short_description,
    long_description=get_readme(),
    license='Apache Software License',
    author='Jens Klein',
    author_email='jens@bluedynamics.com',
    url='http://pypi.python.org/pypi/colddlective.recipe.appengine/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    namespace_packages=['collective', 'collective.recipe'],
    install_requires=[
        'setuptools',
        'zc.buildout>=2.0.1',
        'zc.recipe.egg>=2.0.0.a3',
        'hexagonit.recipe.download',
    ],
    entry_points={
        'zc.buildout': [
            'default = collective.recipe.appengine.tools:Recipe',
            'tools = collective.recipe.appengine.tools:Recipe',
            'sdk = collective.recipe.appengine.sdk:Recipe',
            'app_lib = collective.recipe.appengine.app_lib:Recipe',
        ],
    },
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
