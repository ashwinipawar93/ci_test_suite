import re
import sys
import os
from subprocess import call

import setuptools
from setuptools.command.install import install

package_to_install = [
        'ci_test_suite',
        'ci_test_suite.psu',
        'ci_test_suite.communication',
        'ci_test_suite.communication.ethercat',
        'ci_test_suite.communication.uart',
    ]

with open('src/ci_test_suite/__init__.py', 'r') as f:
    version_file = f.read()
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M).group(1)

if os.path.isfile('requirements.txt'):
    with open('requirements.txt', 'r') as f:
        requirements = f.read().splitlines()
else:
    requirements = ""

def install_requirements(requirements):
    for r in requirements:
        call([sys.executable, '-m', 'pip', 'install', r])

setuptools.setup(
    name='ci_test_suite',
    version=version,
    package_dir={'':'src'},
    packages=package_to_install,
    install_requires=requirements,
    license='MIT',
    author='Ash',
    author_email='gouri.pawar93@gmail.com',
    description="A collection of different scripts and drivers (PSU, EtherCAT)",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
    keywords=['power supply unit', 'psu', 'daq', 'Elektronik-Automation', 'EtherCAT', 'IgH'],
)
