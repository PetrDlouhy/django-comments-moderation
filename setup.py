# -*- coding: utf-8 -*-
#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys


# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv:
    try:
        os.chdir('comments_moderation')
        from django.core import management
        management.call_command('compilemessages')
    finally:
        os.chdir('..')


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")

setup(
    name='django-comments-moderation',
    version=find_version('comments_moderation', '__init__.py'),
    license='GNU Affero General Public License, Version 3.0',

    install_requires=[
        'django-fluent-comments>=0.9.2',
    ],
    requires=[
        'Django (>=1.3)',
    ],
    description='Moderation plugin for django-fluent-comments',
    long_description=read('README.rst'),

    author='Petr Dlouhý',
    author_email='petr.dlouhy@email.cz',

    url='https://github.com/PetrDlouhy/django-comments-moderation',
    download_url='',

    packages=find_packages(exclude=('',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
