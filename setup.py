from setuptools import setup, find_packages

version = '0.4'

setup(
    name='py-configuration',
    version=version,
    packages=find_packages(exclude=['tests*']),
    keywords='yaml config parser',
    license='MIT',
    description='A small python package for using yaml based config files',
    long_description=open('README.md').read(),
    install_requires=['pyyaml'],
    url='https://github.com/tvdsluijs/py-configuration',
    author='Theo van der Sluijs',
    author_email='theo@vandersluijs.nl'
)