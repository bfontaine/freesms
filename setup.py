# -*- coding: UTF-8 -*-

import io
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='freesms/__init__.py'
# In Python 2.x open() doesn't support the encoding keyword parameter.
verstrline = io.open(VERSIONFILE, encoding='utf-8').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='freesms',
    version=verstr,
    author='Baptiste Fontaine',
    author_email='b@ptistefontaine.fr',
    packages=['freesms'],
    url='https://github.com/bfontaine/freesms',
    license=io.open('LICENSE', encoding='utf-8').read().encode("utf-8"),
    description='Send SMS with Free Mobile',
    long_description="""\
freesms is a Python interface to Free mobile SMS API.""",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
