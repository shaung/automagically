# coding: utf8

__VERSION__ = '0.0.1'

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

params = {
    'name': 'automagically',
    'version': __VERSION__,
    'description': '',
    'long_description': read('README.md'),
    'author': 'shaung',
    'author_email': 'shaun.geng@gmail.com',
    'url': 'https://github.com/shaung/automagically/',
    'py_modules': ['automagically'],
    'license': 'BSD',
    'download_url': '',
    'zip_safe': False,
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    'install_requires': [
        'byteplay',
    ],
}

from setuptools import setup
setup(**params)
