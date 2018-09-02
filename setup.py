#!/usr/bin/env python3
from setuptools import setup

setup(
    name='kmd-csvnormalizer',
    version='0.0.0.path',
    description='CSV Normalizer',
    author='Krista Davis',
    url='https://github.com/anybodys/kmd-csvnormalizer',
    packages=['csvnormalizer'],
    install_requires=[],
    python_requires='>=3',
    entry_points={
	'console_scripts': [
	    'kmd-csvnormalizer = csvnormalizer.__main__:main',
	],
    },
    test_suite='tests',
)
