import pip

def search(package):
    print('Searching for %s' % package)
    pip.main(['search', package])
