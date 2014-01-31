#!/usr/bin/env python
import os
from docopt import docopt
import sys

#from ppm import install, search
from install import *
from search import search

doc = """Usage:
  ppm install
  ppm install <package> [--global]
  ppm search <package>
  ppm (-h | --help)
  ppm --version

  Options:
    --global    install packages global
"""

def load_json_config():
    pass

def load_txt_config():
    pass

def main():
    arguments = docopt(doc, version='Python Package Manager 0.1')
    if arguments['install']:
        if arguments['<package>']:
            install(arguments['<package>'])
        else:
            #find requirements.txt
            #find package.json
            #load dependence list
            #call install for all deps
            pass
    elif arguments['search']:
        if arguments['<package>']:
            search(arguments['<package>'])

    return 1

if __name__ == '__main__':
    ret = main()
    if ret:
        sys.exit(ret)