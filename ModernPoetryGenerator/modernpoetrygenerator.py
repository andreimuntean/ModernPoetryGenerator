#!/usr/bin/python3

"""modernpoetrygenerator.py: Generates modern poetry."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

from sys import argv

def read(path):
    file = open(argv[1]).read()

    # Prevents weird exceptions.
    return file.encode('ascii', 'ignore')

def to_modern_poetry(source_text):
    modern_poetry = source_text

    # Decapitalizes the text to express sorrow.
    modern_poetry = modern_poetry.lower()

    return modern_poetry

if len(argv) == 2:
    source_text = read(argv[1])
    modern_poetry = to_modern_poetry(source_text)
    print(modern_poetry)
else:
    print('Please specify a valid file path.')