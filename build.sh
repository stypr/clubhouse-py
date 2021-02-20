#!/bin/sh

rm -rf build/ dist/
rm *.pyc
python3 -OO -m PyInstaller --onefile ./cli.py
