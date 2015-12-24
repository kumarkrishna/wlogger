#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Setup file for Wlogger """
import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('For installation, run \'python setup.py install\'')
    print()

sys.path.insert(0, 'wlogger')
import release

if __name__ == "__main__":
    setup(
        name = release.name,
        version = release.__version__,
        author = release.__author__,
        author_email = release.__email__,
        description = release.__description__,
        url='https://github.com/kumarkrishna/wlogger',
        keywords='wlogger work logger todo project reminder',
        packages = ['wlogger'],
        entry_points = {
            'console_scripts': [
            'wlogger = wlogger.log:main'            ]
        },
        license = 'Apache License',
        # install_requires = ['phonenumbers', 'requests', 'pycrypto',
                            # 'python-dateutil', 'parsedatetime'],
        # test_suite = 'nose.collector',
        # tests_require = ['nose>=0.10.1']
    )
