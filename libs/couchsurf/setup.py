import setuptools

packages = setuptools.find_packages(where='./src')

setuptools.setup(
    name="CouchSurf",
    version="0.1",
    packages=packages,
    include_package_data=True,
    description='Limited API for basic CouchDB operations.',
    long_description=open('README.md', 'r').read(),
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()]
 )
