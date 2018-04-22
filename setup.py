#!/usr/bin/env python3

import os

from setuptools import setup, find_packages

def read(filename):
    """Utility function to read the README file.

    Args:
        fname (str): The name of the file to read.

    Returns:
        str: The content of the file.

    """
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="gen-cisco",
    version="1.0",
    description="Generates Cisco scripts based on an INI file",
    author="Terencio Agozzino",
    author_email="terencio.agozzino@gmail.com",
    license="MIT",
    keywords = "cisco ccna generate netacad packettracer python script scripts",
    url="https://github.com/rememberYou/gen-cisco",
    packages=find_packages(),
    long_description=read('README.md'),
    scripts=['gen-cisco.py'],
    install_requires=['click'],
    package_data={
        'src': ['*.txt'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha"
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
