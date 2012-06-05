#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import autocompleteinputs

setup(
    name = 'django-autocompleteinputs',
    version = ":versiontools:autocompleteinputs:",
    description = "Autocomplete text field based on jquery-ui",
    long_description = "",
    keywords = 'django, jquery, jquery-ui, autocomplete',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/kaleidos/django-autocompleteinputs',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
