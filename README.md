# freesms

[![Pypi package](https://img.shields.io/pypi/v/freesms.png)](https://pypi.python.org/pypi/freesms)

**`freesms`** is a Python interface for Free Mobile SMS API. If you subscribed to their service it allows you to
programmatically send SMSes to yourself.

Install
-------

    [sudo] pip install freesms

Starting from v0.2.0 the library is only tested on Python 3.x, but it should work on 2.7.

Usage
-----

```python
from freesms import FreeClient

f = FreeClient(user="...", passwd="...")
resp = f.send_sms("hello this is my SMS")
resp.status_code  # 200
```