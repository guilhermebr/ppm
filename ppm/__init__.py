#!/usr/bin/env python
import os
from docopt import docopt
import sys
import re

doc = """Usage:
  ppm install
  ppm install <package-name>
  ppm search <package-name>
  ppm (-h | --help)
  ppm --version
"""

def load_json_config():
    pass

def load_txt_config():
    pass

def install_package(package):
    print('Installing %s' % package)
    #call pip to install package

def main(arguments):
    if arguments['install']:
        if arguments['<package-name>']:
            install_package(arguments['<package-name>'])
        else:
            #find requirements.txt
            #find package.json
            #load dependence list
            #call install_package for all deps
    return 1

if __name__ == '__main__':
    arguments = docopt(doc, version='Python Package Manager 0.1')

    ret = main(arguments)
    if ret:
        sys.exit(ret)