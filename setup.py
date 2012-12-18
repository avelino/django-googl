#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages



version = '0.1'
description = u"Django goo.gl app"

classifiers = ['Environment :: Plugins',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',]

long_description = description
try:
    long_description = open('README.md').read()
except:
    pass

setup(name='django-googl',
    version = version,
    description = description,
    long_description = long_description,
    classifiers = classifiers,
    keywords = 'django apps googl google api ',
    author = 'Thiago Avelino',
    author_email = 'thiagoavelinoster@gmail.com',
    url = 'https://github.com/avelino/django-googl/',
    download_url = "https://github.com/avelino/django-googl/tarball/master",
    license = 'BSD',
    packages = find_packages(),
    package_dir = {'googl': 'googl'},
    include_package_data = True,
)
