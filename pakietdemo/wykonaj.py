#!/usr/bin/python

import re
import os

here = os.path.abspath(os.path.dirname(__file__))
version = re.search(
    '^__version__\s*=\s*"(.*)"', open(os.path.join(here, "__init__.py")).read(), re.M
).group(1)
release = re.search(
    '^__release__\s*=\s*"(.*)"', open(os.path.join(here, "__init__.py")).read(), re.M
).group(1)
__version__ = version
__release__ = release


def main():
    print("Pakiet demonstracyjny %s" % __release__)

