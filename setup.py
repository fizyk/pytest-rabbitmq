# -*- coding: utf-8 -*-
# Copyright (C) 2016 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).

# This file is part of pytest-rabbitmq.

# pytest-rabbitmq is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pytest-rabbitmq is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with pytest-rabbitmq. If not, see <http://www.gnu.org/licenses/>.


import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


def read(fname):
    """
    Read given file's content.

    :param str fname: file name
    :returns: file contents
    :rtype: str
    """
    return open(os.path.join(here, fname)).read()


requirements = []

test_requires = [
    'pytest',
    'pytest-cov'
]

extras_require = {
    'docs': ['sphinx'],
    'tests': test_requires
}

setup(
    name='pytest-rabbitmq',
    version='0.0.0',
    description='RabbitMQ process and client fixtures for pytest',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
    ),
    keywords='RabbitMQ process and client fixtures for pytest',
    author='Clearcode - The A Room',
    author_email='thearoom@clearcode.cc',
    url='https://github.com/ClearcodeHQ/pytest-rabbitmq',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    tests_require=test_requires,
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
)
