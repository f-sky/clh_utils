#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required for fairseq.')

setup(
    name='myutils',
    version='0.0.1',
    description='Chenlinghao\'s personal utils.',
    packages=find_packages(),
    install_requires=[
        'torch',
        'matplotlib',
        'numpy',
        'visdom'
    ]
)
# to install this, use 'python setup.py build develop'
# to add a new module, write a script in myutils/myutils directory, then import it in __init__.py, then install it .
