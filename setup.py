#!/usr/bin/env python3
from contextlib import suppress

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pip._internal.req import parse_requirements  # pip>9.0.3
except ImportError:
    from pip.req import parse_requirements  # pip<=9.0.3

try:
    from pip._internal.download import PipSession  # pip>9.0.3
except ImportError:
    with suppress(ImportError):
        from pip.download import PipSession  # pip<=9.0.3


REQUIREMENTS_TXT = 'requirements.txt'


try:
    requirements = list(parse_requirements(REQUIREMENTS_TXT))
except TypeError:
    requirements = parse_requirements(REQUIREMENTS_TXT, session=PipSession())

required, dependency_links = [], []
for item in requirements:
    # We want to handle package names and also repo URLs.
    if getattr(item, 'url', None):  # older pip has URL
        dependency_links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        dependency_links.append(str(item.link))
    if item.req:
        required.append(str(item.req))


setup(
    install_requires=required,
    dependency_links=dependency_links,
)
