#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup



version = '0.1'
description = u"Django goo.gl app"

setup(name='django-googl',
    version = version,
    description = description,
    long_description = (''),
    classifiers = [
      'Environment :: Plugins',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],
    keywords = 'django apps googl google api',
    author = 'Thiago Avelino',
    author_email = 'thiagoavelinoster@gmail.com',
    url = 'https://github.com/avelino/django-googl',
    download_url = "https://github.com/avelino/django-googl/archive/master.zip",
    license = 'BSD',
    packages = ['googl'],
    package_dir = {'googl': 'googl'},
    include_package_data = True,
    zip_safe = False,
    install_requires = ['setuptools'],
)
