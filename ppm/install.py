import os
import pip
from virtualenv import create_environment


def install(package):
    if not os.path.exists('.env'):
        print('Creating virtualenv')
        create_environment('.env', never_download=True)

    print('Installing %s' % package)
    pip.main(['install', package, '-t',  os.environ['PWD'] + '/.env/lib/python2.7/site-packages/','--log-file', '.env/ppm.log'])

