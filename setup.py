#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of flask-debugtb-elasticsearch.
# https://github.com/heynemann/flask-debugtb-elasticsearch

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from setuptools import setup, find_packages
from flask_debugtb_elasticsearch import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='flask-debugtb-elasticsearch',
    version=__version__,
    description='Flask debug toolbar panel for elasticsearch queries.',
    long_description='''
Flask debug toolbar panel for elasticsearch queries.
''',
    keywords='flask elasticsearch debug toolbar',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='https://github.com/heynemann/flask-debugtb-elasticsearch',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'flask-debugtb-elasticsearch=flask_debugtb_elasticsearch.cli:main',
        ],
    },
)
