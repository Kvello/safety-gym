#!/usr/bin/env python

from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safety_gym',
    packages=['safety_gym'],
    install_requires=[
        'gym~=0.25.2',
        'joblib~=1.4.2',
        'mujoco_py~=2.1.2',
        'numpy~=1.19.2',
        'xmltodict~=0.14.2',
    ],
)