# -*- coding: UTF-8 -*-

from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='freesms/__init__.py'
verstrline = open(VERSIONFILE).read()
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
    license="MIT",
    description='Send SMS with Free Mobile',
    install_requires=["requests"],
    long_description="""\
freesms is a Python interface to Free mobile SMS API.""",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
