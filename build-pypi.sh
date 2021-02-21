#!/bin/bash

rm -rf dist
rm -rf clubhouse_py.egg-info
python setup.py sdist
twine upload dist/*
