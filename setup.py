#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import setup, find_packages


BIN_FOLDER = 'bin'


def readme():
    with open('README.md') as f:
        return f.read()


def apply_folder_join(item):
    return os.path.join(BIN_FOLDER, item)


if os.name == 'nt':
    bin_scripts = ['symoro-bin.py']
else:
    bin_scripts = ['symoro-bin']
bin_scripts = [apply_folder_join(x) for x in bin_scripts]

setup(
    name='symoro',
    version='mine',
    description='SYmoblic MOdelling of RObots software package',
    url='https://github.com/xu-yang16/symoro-python3',
    license='MIT',
    scripts=bin_scripts,
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=[
        'sympy==1.11rc1',
        'numpy==1.23.2',
        'wxPython==4.0.7',
        'PyOpenGL==3.1.6'
    ],
    zip_safe=False
)


