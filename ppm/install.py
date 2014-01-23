import pip

def install(package):
    print('Installing %s' % package)
    pip.main(['install', package, '-t', 'python_modules', '--log-file', 'ppm.log'])
