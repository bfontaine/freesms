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

``freesms`` is a Python interface for Free Mobile SMS API. If you subscribed to
their service it allows you to programmatically send SMSes to yourself.

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
    resp = f.send_sms("hello this is my SMS")
    resp.status_code  # 200
