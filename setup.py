import os
import pakietdemo
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='PakietDemo',
    version=pakietdemo.__version__,
    description='Aplikacja: pakiet demonstracyjny',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python", ],
    author='Piotr Czaja',
    author_email='czaja_piotr@o2.pl',
    url='http://piotr.czaja.link',
    keywords='python',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['wykonaj-pakiet-demo = pakietdemo.wykonaj:main', ]
        },
    platforms='any',
      )
