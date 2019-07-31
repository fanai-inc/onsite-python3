#!/usr/bin/env python3
"""
setup.py

Inspired by:
    https://github.com/kennethreitz/setup.py

"""
import os.path

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

try:
    from pip.download import PipSession
except ImportError:
    try:
        from pip._internal.download import PipSession
    except ImportError:
        pass


# Package meta-data.
NAME = 'myproj'
DESCRIPTION = 'FanAI onsite interview'
URL = 'https://github.com/fanai-inc/onsite-python3'
EMAIL = 'derek@fan.ai'
AUTHOR = 'Derek M Frank'


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for
# that!


def _read(filename, parent=None):
    parent = parent or __file__

    try:
        with open(os.path.join(os.path.dirname(parent), filename)) as f:
            return f.read()
    except IOError:
        return ''


# What packages are required for this module to be executed?  Not development.
# If this is an application, then specify requirements/lock.txt,
# otherwise, specify requirements/common.in if a library.
req_path = os.path.join('requirements', 'lock.txt')

try:
    requirements = list(parse_requirements(req_path))
except TypeError:
    requirements = parse_requirements(req_path, session=PipSession())

required, dependency_links = [], []
for item in requirements:
    # We want to handle package names and also repo URLs.
    if getattr(item, 'url', None):  # older pip has URL
        dependency_links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        dependency_links.append(str(item.link))
    if item.req:
        required.append(str(item.req))


# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in
# file!
long_description = '\n' + _read('README.rst')
license = _read('LICENSE')


# Load the package's __version__.py module as a dictionary.
about = {}
exec(_read(os.path.join(NAME, '__version__.py')), about)  # nosec: B102


# Where the magic happens.
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests', 'docs', 'requirements')),
    python_requires='>= 3.7.4',
    install_requires=required,
    dependency_links=dependency_links,
    include_package_data=True,
    license=license,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
