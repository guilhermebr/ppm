#!/usr/bin/env python

from setuptools import setup

requirements = [
    "docopt>=0.6.1",
    "virtualenv",
    ]

setup(name='ppm',
      version='1.0',
      description='Python Package Manager',
      author='Guilherme Rezende',
      author_email='guilhermebr@gmail.com',
      url='http://github.com/guilhermebr/ppm',
      install_requires=requirements,
      packages=['ppm'],
      entry_points={
        "console_scripts": [
            "ppm=ppm:main",
        ],
      },
     )