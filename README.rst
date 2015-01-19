=======
freesms
=======

.. image:: https://img.shields.io/travis/bfontaine/freesms.png
   :target: https://travis-ci.org/bfontaine/freesms
   :alt: Build status

.. image:: https://coveralls.io/repos/bfontaine/freesms/badge.png?branch=master
   :target: https://coveralls.io/r/bfontaine/freesms?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/freesms.png
   :target: https://pypi.python.org/pypi/freesms
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/freesms.png
   :target: https://pypi.python.org/pypi/freesms

``freesms`` is a compact trie implementation in Python.

Install
-------

.. code-block::

    [sudo] pip install freesms

The library works with Python 2.7 and 3.x.

Usage
-----

.. code-block::

    from freesms import FreeClient

    f = FreeClient(user="...", passwd="...")

    f.send_sms("hello this is my SMS")
