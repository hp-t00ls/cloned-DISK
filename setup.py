#!/usr/bin/env python

from setuptools import setup, Extension, find_packages
import os
import sys

setup(
    name='DISK',
    version='0.1',
    description="Deep Imputation of SKeleton data - Personal Fork",
    long_description="Personal fork and modifications of the DISK project for skeleton data imputation",
    author='Hippolyte',
    author_email="hippolyte.pascal@edu.esiee.fr",
    packages=find_packages("."),
    url="https://github.com/hp-t00ls/cloned-DISK",
    install_requires=[],
    package_data={'DISK': ['resources/*']},
    entry_points={'console_scripts': [
        "DISK = DISK.launchers.DISK_launcher:main",
    ]},
)
