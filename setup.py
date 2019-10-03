#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ucbviz2019',
    version='0.0.1',
    description='Entry for UC Berkeley Graduate Data Visualization Contest',
    long_description=readme,
    author='Alexander Dunn, John Dagdelen',
    author_email='ardunn@lbl.gov, jdagdelen@lbl.gov',
    url='https://github.com/ardunn/ucbviz2019',
    license=license,
    packages=find_packages()
)
