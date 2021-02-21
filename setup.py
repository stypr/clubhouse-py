#!/usr/bin/python -u
#-*- coding: utf-8 -*-
"""
    setup.py
    For pypi
"""
from distutils.core import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clubhouse-py",
    packages=["clubhouse-py"],
    version="304",
    license="MIT",
    description=("Clubhouse API written in Python. Standalone client included." +
        "For reference and education purposes only."),
    author="Harold Kim",
    author_email="root@stypr.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stypr/clubhouse-py",
    download_url="https://github.com/stypr/clubhouse-py/archive/v304.tar.gz",
    keywords=[
        "clubhouse",
        "voice-chat",
        "clubhouse-client",
        "clubhouse-api",
        "clubhouse-lib",
    ],
    install_requires=[
        "keyboard",
        "requests",
        "rich",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
