from __future__ import absolute_import, print_function
from setuptools import setup, find_packages

setup (
    name='gha_test',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
    ],
)
