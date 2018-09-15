# -*- coding: UTF-8 -*-

import unittest
from httmock import all_requests, response, HTTMock
from requests import exceptions

from freesms import FreeClient, FreeResponse

CODES = [200, 400, 500]
EXCEPTIONS = (('Request', exceptions.RequestException),
              ('Connection', exceptions.ConnectionError),
              ('Timeout', exceptions.Timeout))


@all_requests
def smsapi_mock(url, request):
    qry = url.query
    for code in CODES:
        if "code%s" % code in qry:
            return response(code)
    for name, exc in EXCEPTIONS:
        if "exception%s" % name in qry:
                raise exc
    return response(404)


class TestSMS(unittest.TestCase):

    def setUp(self):
        self.client = FreeClient(user="someuser", passwd="secret")

    def test_500(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops code500 error")

        self.assertFalse(bool(resp))
        self.assertEquals(resp.status_code, 500)
        self.assertFalse(resp.success())
        self.assertTrue(resp.error())

    def test_400(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops code400 error")

        self.assertFalse(bool(resp))
        self.assertEquals(resp.status_code, 400)

    def test_200(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops code200 error")

        self.assertTrue(bool(resp))
        self.assertEquals(resp.status_code, 200)
        self.assertTrue(resp.success())
        self.assertFalse(resp.error())

    def test_py2_bool_resp(self):
        ok = FreeResponse(200)
        ko = FreeResponse(400)

        self.assertTrue(ok.__nonzero__())
        self.assertFalse(ko.__nonzero__())

    def test_py3_bool_resp(self):
        ok = FreeResponse(200)
        ko = FreeResponse(400)

        self.assertTrue(ok.__bool__())
        self.assertFalse(ko.__bool__())

    def test_connection_error(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops exceptionConnectionError")

        self.assertFalse(bool(resp))
        self.assertEquals(resp.status_code, 444)

    def test_timeout_error(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops exceptionTimeout")

        self.assertFalse(bool(resp))
        self.assertEquals(resp.status_code, 499)

    def test_requests_error(self):
        with HTTMock(smsapi_mock):
            resp = self.client.send_sms("oops exceptionRequest")

        self.assertFalse(bool(resp))
        self.assertEquals(resp.status_code, 444)
