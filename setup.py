# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages
from setuptools.dist import Distribution

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.rst")) as f:
        README = f.read()
except IOError:
    README = ""

try:
    with open(os.path.join(here, "CHANGES.txt")) as f:
        CHANGES = f.read()
except IOError:
    CHANGES = ""


"""
NOTE: keep requirements_dev.txt and the *_requires lists below in sync

for future reference:
from pip.req import parse_requirements
install_requires =  parse_requirements(<requirements_path>)
"""



install_requires = [
    "sqlalchemy>=1.4.0",
    "pyyaml>=6.0"
]

docs_extras = []

tests_require = [
    "pytest>=7.0.0"
]

testing_extras = tests_require + []

setup_kwargs = {
    "name": "swagger-dialect",
    "version": open("VERSION").read().strip(),
    "description": "Swagger SQLAlchemy dialect and DBAPI to Swagger YAML file",
    "long_description": README + "\n\n" + CHANGES,
    "python_requires": ">3.10.0",
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Database :: Front-Ends",
    ],
    "keywords": "import, physical address, file path",
    "author": "robertbetts",
    "url": "https://github.com/robertbetts/swagger-dialect",
    "packages": find_packages(),
    "include_package_data": True,
    "zip_safe": False,
    "install_requires": install_requires,
    "extras_require": {"testing": testing_extras, "docs": docs_extras},
    "tests_require": tests_require,
    "test_suite": "tests",
    "entry_points": "",
}

setup(**setup_kwargs)


