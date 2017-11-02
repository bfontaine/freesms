# -*- coding: UTF-8 -*-

"""
This module provides a Python interface to Free Mobile SMS API.
See:
    http://mobile.free.fr/

.. moduleauthor:: Baptiste Fontaine <b@ptistefontaine.fr>
"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

__version__ = '0.1.1'


class FreeResponse(object):
    """
    An API call response. This is a boolean-like with a ``status_code``
    attribute.
    """

    def __init__(self, code):
        """
        Create a new response from the given status code.
        """
        self.status_code = code

    def success(self):
        return self.status_code == 200

    def error(self):
        """
        Return true only if this response don't have a 200 (OK) status code.
        """
        return not self.success()

    def __nonzero__(self):
        """
        Alias for ``.success()``. This allows you to use a ``FreeResponse`` as
        a boolean-like: it'll be falsy if there was an error, truthy if not.
        """
        return self.success()

    def __bool__(self):
        """
        See ``__nonzero__`` (this is for Python 3 compatibility).
        """
        return self.__nonzero__()


class FreeClient(object):
    BASE_URL = 'https://smsapi.free-mobile.fr/sendmsg'

    def __init__(self, user, passwd):
        """
        Create a new Free Mobile SMS API client. Each client is tied to a phone
        number.
        """
        self._user = user
        self._passwd = passwd

    def send_sms(self, text, **kw):
        """
        Send an SMS. Since Free only allows us to send SMSes to ourselves you
        don't have to provide your phone number.
        """

        params = {
            'user': self._user,
            'pass': self._passwd,
            'msg': text
        }

        kw.setdefault("verify", False)

        if not kw["verify"]:
            # remove SSL warning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        res = requests.get(FreeClient.BASE_URL, params=params, **kw)
        return FreeResponse(res.status_code)
