# freesms

[![Pypi package](https://img.shields.io/pypi/v/freesms.png)](https://pypi.python.org/pypi/freesms)

**`freesms`** is a Python interface for Free Mobile SMS API. If you subscribed to their service it allows you to
programmatically send SMSes to yourself.

Install
-------

    [sudo] pip install freesms

The library works with Python 2.7 and 3.x.

Usage
-----

```python
from freesms import FreeClient

f = FreeClient(user="...", passwd="...")
resp = f.send_sms("hello this is my SMS")
resp.status_code  # 200
```