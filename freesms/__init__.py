"""
This module provides a Python interface to Free Mobile SMS API.
See:
    https://mobile.free.fr/

.. moduleauthor:: Baptiste Fontaine <b@ptistefontaine.fr>
"""

import requests

__version__ = '0.3.0'


class FreeResponse:
    """
    An API call response. This is a boolean-like with a ``status_code``
    attribute.
    """

    def __init__(self, response: requests.Response):
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

    __bool__ = success


class FreeClient:
    BASE_URL = 'https://smsapi.free-mobile.fr/sendmsg'

    def __init__(self, user: str,
                 password: str | None = None,
                 passwd: str | None = None):
        """
        Create a new Free Mobile SMS API client. Each client is tied to a phone number.

        :param user: username
        :param password: password
        :param passwd: alias for ``password``.
        """
        assert password is not None or passwd is not None, \
            "The password cannot be None."

        self._user = user
        self._password = password or passwd

    def send_sms(self, text: str, **kwargs):
        """
        Send an SMS. Free only allows us to send SMSes to oneself, so you don't have to provide your phone number.

        :param text: text of the message
        :param kwargs: keyword arguments passed to the underlying ``requests.get`` call
        :return: FreeResponse
        """

        params = {
            'user': self._user,
            'pass': self._password,
            'msg': text
        }

        response = requests.get(self.BASE_URL, params=params, **kwargs)
        return FreeResponse(response)
