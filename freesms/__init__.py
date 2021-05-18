# -*- coding: UTF-8 -*-

"""
This module provides a Python interface to Free Mobile SMS API.
See:
    https://mobile.free.fr/

.. moduleauthor:: Baptiste Fontaine <b@ptistefontaine.fr>
"""

import requests

__version__ = '0.2.0'


class FreeResponse(object):
    """
    An API call response. This is a boolean-like with a ``status_code``
    attribute.
    """

    def __init__(self, response):
        """
        :param response: requests.Response object
        """
        self._response = response

    @property
    def status_code(self):
        return self._response.status_code

    def success(self):
        return self._response.ok

    def error(self):
        """
        Return true only if this response don't have a 20x (OK and similar) status code.
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

    def send_sms(self, text, **kwargs):
        """
        Send an SMS. Since Free only allows us to send SMSes to oneself
        you don't have to provide your phone number.

        :param text: text of the message
        :param kwargs: keyword arguments passed to the underlying ``requests.get`` call
        :return: FreeResponse
        """

        params = {
            'user': self._user,
            'pass': self._passwd,
            'msg': text
        }

        response = requests.get(self.BASE_URL, params=params, **kwargs)
        return FreeResponse(response)
