#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pystanbol',
    version='0.1',
    description='A python REST components for Apache Stanbol',
    author='Athento',
    author_email='rh@athento.com',
    url='http://github.com/athento/pystanbol',
    license='Apache 2.0 License',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Semantic Tagging'
    ],
    packages=find_packages(),
    install_requires=[
        'restkit',
        'socketpool',
        'rdflib',
        'eventlet'
    ],
    extras_require={
        'test': [
            'pytest',
            'mock'
        ],
    },
)
